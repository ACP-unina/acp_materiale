#!/usr/bin/env python3
import multiprocessing as mp
import os
import platform
import statistics
import sys
import time
from concurrent.futures import ProcessPoolExecutor


def noop():
    return None


def small_task(x):
    return x + 1


def cpu_task(n: int) -> int:
    acc = 0
    for i in range(n):
        acc += (i * i) % 97
    return acc


def payload_task(data):
    return len(data)


def timed(fn, repeat=3):
    samples = []
    for _ in range(repeat):
        t0 = time.perf_counter()
        fn()
        samples.append(time.perf_counter() - t0)
    return {
        "min": min(samples),
        "mean": statistics.mean(samples),
        "max": max(samples),
        "samples": samples,
    }


def benchmark_startup(ctx_name: str, nproc: int, repeat: int):
    ctx = mp.get_context(ctx_name)

    def run():
        procs = [ctx.Process(target=noop) for _ in range(nproc)]
        for p in procs:
            p.start()
        for p in procs:
            p.join()

    return timed(run, repeat=repeat)


def benchmark_pool_small_tasks(ctx_name: str, ntasks: int, workers: int, repeat: int):
    ctx = mp.get_context(ctx_name)

    def run():
        with ProcessPoolExecutor(max_workers=workers, mp_context=ctx) as ex:
            list(ex.map(small_task, range(ntasks)))

    return timed(run, repeat=repeat)


def benchmark_pool_cpu(ctx_name: str, workers: int, n_per_worker: int, repeat: int):
    ctx = mp.get_context(ctx_name)

    def run():
        with ProcessPoolExecutor(max_workers=workers, mp_context=ctx) as ex:
            list(ex.map(cpu_task, [n_per_worker] * workers))

    return timed(run, repeat=repeat)


def benchmark_large_payload(ctx_name: str, workers: int, payload_size: int, repeat: int):
    ctx = mp.get_context(ctx_name)
    payload = list(range(payload_size))

    def run():
        with ProcessPoolExecutor(max_workers=workers, mp_context=ctx) as ex:
            list(ex.map(payload_task, [payload] * workers))

    return timed(run, repeat=repeat)


def fmt(stats_dict):
    return (
        f"min={stats_dict['min']:.4f}s  "
        f"mean={stats_dict['mean']:.4f}s  "
        f"max={stats_dict['max']:.4f}s"
    )


def main():
    available = mp.get_all_start_methods()
    cpu_count = os.cpu_count() or 1

    print("=" * 72)
    print("multiprocessing start method benchmark")
    print("=" * 72)
    print(f"Python      : {sys.version.splitlines()[0]}")
    print(f"Executable  : {sys.executable}")
    print(f"Platform    : {platform.platform()}")
    print(f"CPU count   : {cpu_count}")
    print(f"Available   : {available}")
    print(f"Default     : {mp.get_start_method(allow_none=True)}")
    print()

    # Tune these if you want a longer or shorter benchmark.
    nproc_startup = min(8, cpu_count)
    pool_workers = min(4, cpu_count)
    repeats = 3
    ntasks_small = 5000
    cpu_iters = 2_000_000
    payload_size = 1_000_000

    print("Settings")
    print(f"  startup processes : {nproc_startup}")
    print(f"  pool workers      : {pool_workers}")
    print(f"  repeats           : {repeats}")
    print(f"  small tasks       : {ntasks_small}")
    print(f"  cpu iterations    : {cpu_iters} per worker")
    print(f"  payload size      : {payload_size} ints")
    print()

    results = {}

    for method in available:
        print(f"--- {method} ---")
        results[method] = {}

        try:
            r = benchmark_startup(method, nproc_startup, repeats)
            results[method]["startup"] = r
            print(f"startup overhead    {fmt(r)}")
        except Exception as e:
            print(f"startup overhead    ERROR: {e}")

        try:
            r = benchmark_pool_small_tasks(method, ntasks_small, pool_workers, repeats)
            results[method]["small_tasks"] = r
            print(f"small task pool     {fmt(r)}")
        except Exception as e:
            print(f"small task pool     ERROR: {e}")

        try:
            r = benchmark_pool_cpu(method, pool_workers, cpu_iters, repeats)
            results[method]["cpu_bound"] = r
            print(f"cpu-bound pool      {fmt(r)}")
        except Exception as e:
            print(f"cpu-bound pool      ERROR: {e}")

        try:
            r = benchmark_large_payload(method, pool_workers, payload_size, repeats)
            results[method]["large_payload"] = r
            print(f"large payload pool  {fmt(r)}")
        except Exception as e:
            print(f"large payload pool  ERROR: {e}")

        print()

    print("=" * 72)
    print("Quick interpretation")
    print("=" * 72)
    print(
        "- startup overhead shows process creation cost only\n"
        "- small task pool punishes methods with higher startup/serialization overhead\n"
        "- cpu-bound pool reduces startup importance and highlights steady-state execution\n"
        "- large payload pool shows pickling / IPC cost, usually worst for spawn"
    )
    print()
    print("Typical outcome on Unix:")
    print("  fork       fastest startup")
    print("  forkserver middle")
    print("  spawn      slowest startup")
    print()
    print("But always benchmark on your machine and workload.")


if __name__ == "__main__":
    main()
