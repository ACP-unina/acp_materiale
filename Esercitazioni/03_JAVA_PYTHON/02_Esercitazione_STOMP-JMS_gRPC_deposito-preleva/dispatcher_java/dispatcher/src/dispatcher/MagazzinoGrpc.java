package dispatcher;

import static io.grpc.MethodDescriptor.generateFullMethodName;
import static io.grpc.stub.ClientCalls.asyncBidiStreamingCall;
import static io.grpc.stub.ClientCalls.asyncClientStreamingCall;
import static io.grpc.stub.ClientCalls.asyncServerStreamingCall;
import static io.grpc.stub.ClientCalls.asyncUnaryCall;
import static io.grpc.stub.ClientCalls.blockingServerStreamingCall;
import static io.grpc.stub.ClientCalls.blockingUnaryCall;
import static io.grpc.stub.ClientCalls.futureUnaryCall;
import static io.grpc.stub.ServerCalls.asyncBidiStreamingCall;
import static io.grpc.stub.ServerCalls.asyncClientStreamingCall;
import static io.grpc.stub.ServerCalls.asyncServerStreamingCall;
import static io.grpc.stub.ServerCalls.asyncUnaryCall;
import static io.grpc.stub.ServerCalls.asyncUnimplementedStreamingCall;
import static io.grpc.stub.ServerCalls.asyncUnimplementedUnaryCall;

/**
 */
@javax.annotation.Generated(
    value = "by gRPC proto compiler (version 1.9.1)",
    comments = "Source: magazzino.proto")
public final class MagazzinoGrpc {

  private MagazzinoGrpc() {}

  public static final String SERVICE_NAME = "dispatcher.Magazzino";

  // Static method descriptors that strictly reflect the proto.
  @io.grpc.ExperimentalApi("https://github.com/grpc/grpc-java/issues/1901")
  @java.lang.Deprecated // Use {@link #getDepositaMethod()} instead. 
  public static final io.grpc.MethodDescriptor<dispatcher.Articolo,
      dispatcher.Empty> METHOD_DEPOSITA = getDepositaMethod();

  private static volatile io.grpc.MethodDescriptor<dispatcher.Articolo,
      dispatcher.Empty> getDepositaMethod;

  @io.grpc.ExperimentalApi("https://github.com/grpc/grpc-java/issues/1901")
  public static io.grpc.MethodDescriptor<dispatcher.Articolo,
      dispatcher.Empty> getDepositaMethod() {
    io.grpc.MethodDescriptor<dispatcher.Articolo, dispatcher.Empty> getDepositaMethod;
    if ((getDepositaMethod = MagazzinoGrpc.getDepositaMethod) == null) {
      synchronized (MagazzinoGrpc.class) {
        if ((getDepositaMethod = MagazzinoGrpc.getDepositaMethod) == null) {
          MagazzinoGrpc.getDepositaMethod = getDepositaMethod = 
              io.grpc.MethodDescriptor.<dispatcher.Articolo, dispatcher.Empty>newBuilder()
              .setType(io.grpc.MethodDescriptor.MethodType.UNARY)
              .setFullMethodName(generateFullMethodName(
                  "dispatcher.Magazzino", "deposita"))
              .setSampledToLocalTracing(true)
              .setRequestMarshaller(io.grpc.protobuf.ProtoUtils.marshaller(
                  dispatcher.Articolo.getDefaultInstance()))
              .setResponseMarshaller(io.grpc.protobuf.ProtoUtils.marshaller(
                  dispatcher.Empty.getDefaultInstance()))
                  .setSchemaDescriptor(new MagazzinoMethodDescriptorSupplier("deposita"))
                  .build();
          }
        }
     }
     return getDepositaMethod;
  }
  @io.grpc.ExperimentalApi("https://github.com/grpc/grpc-java/issues/1901")
  @java.lang.Deprecated // Use {@link #getPrelevaMethod()} instead. 
  public static final io.grpc.MethodDescriptor<dispatcher.Empty,
      dispatcher.Articolo> METHOD_PRELEVA = getPrelevaMethod();

  private static volatile io.grpc.MethodDescriptor<dispatcher.Empty,
      dispatcher.Articolo> getPrelevaMethod;

  @io.grpc.ExperimentalApi("https://github.com/grpc/grpc-java/issues/1901")
  public static io.grpc.MethodDescriptor<dispatcher.Empty,
      dispatcher.Articolo> getPrelevaMethod() {
    io.grpc.MethodDescriptor<dispatcher.Empty, dispatcher.Articolo> getPrelevaMethod;
    if ((getPrelevaMethod = MagazzinoGrpc.getPrelevaMethod) == null) {
      synchronized (MagazzinoGrpc.class) {
        if ((getPrelevaMethod = MagazzinoGrpc.getPrelevaMethod) == null) {
          MagazzinoGrpc.getPrelevaMethod = getPrelevaMethod = 
              io.grpc.MethodDescriptor.<dispatcher.Empty, dispatcher.Articolo>newBuilder()
              .setType(io.grpc.MethodDescriptor.MethodType.UNARY)
              .setFullMethodName(generateFullMethodName(
                  "dispatcher.Magazzino", "preleva"))
              .setSampledToLocalTracing(true)
              .setRequestMarshaller(io.grpc.protobuf.ProtoUtils.marshaller(
                  dispatcher.Empty.getDefaultInstance()))
              .setResponseMarshaller(io.grpc.protobuf.ProtoUtils.marshaller(
                  dispatcher.Articolo.getDefaultInstance()))
                  .setSchemaDescriptor(new MagazzinoMethodDescriptorSupplier("preleva"))
                  .build();
          }
        }
     }
     return getPrelevaMethod;
  }

  /**
   * Creates a new async stub that supports all call types for the service
   */
  public static MagazzinoStub newStub(io.grpc.Channel channel) {
    return new MagazzinoStub(channel);
  }

  /**
   * Creates a new blocking-style stub that supports unary and streaming output calls on the service
   */
  public static MagazzinoBlockingStub newBlockingStub(
      io.grpc.Channel channel) {
    return new MagazzinoBlockingStub(channel);
  }

  /**
   * Creates a new ListenableFuture-style stub that supports unary calls on the service
   */
  public static MagazzinoFutureStub newFutureStub(
      io.grpc.Channel channel) {
    return new MagazzinoFutureStub(channel);
  }

  /**
   */
  public static abstract class MagazzinoImplBase implements io.grpc.BindableService {

    /**
     */
    public void deposita(dispatcher.Articolo request,
        io.grpc.stub.StreamObserver<dispatcher.Empty> responseObserver) {
      asyncUnimplementedUnaryCall(getDepositaMethod(), responseObserver);
    }

    /**
     */
    public void preleva(dispatcher.Empty request,
        io.grpc.stub.StreamObserver<dispatcher.Articolo> responseObserver) {
      asyncUnimplementedUnaryCall(getPrelevaMethod(), responseObserver);
    }

    @java.lang.Override public final io.grpc.ServerServiceDefinition bindService() {
      return io.grpc.ServerServiceDefinition.builder(getServiceDescriptor())
          .addMethod(
            getDepositaMethod(),
            asyncUnaryCall(
              new MethodHandlers<
                dispatcher.Articolo,
                dispatcher.Empty>(
                  this, METHODID_DEPOSITA)))
          .addMethod(
            getPrelevaMethod(),
            asyncUnaryCall(
              new MethodHandlers<
                dispatcher.Empty,
                dispatcher.Articolo>(
                  this, METHODID_PRELEVA)))
          .build();
    }
  }

  /**
   */
  public static final class MagazzinoStub extends io.grpc.stub.AbstractStub<MagazzinoStub> {
    private MagazzinoStub(io.grpc.Channel channel) {
      super(channel);
    }

    private MagazzinoStub(io.grpc.Channel channel,
        io.grpc.CallOptions callOptions) {
      super(channel, callOptions);
    }

    @java.lang.Override
    protected MagazzinoStub build(io.grpc.Channel channel,
        io.grpc.CallOptions callOptions) {
      return new MagazzinoStub(channel, callOptions);
    }

    /**
     */
    public void deposita(dispatcher.Articolo request,
        io.grpc.stub.StreamObserver<dispatcher.Empty> responseObserver) {
      asyncUnaryCall(
          getChannel().newCall(getDepositaMethod(), getCallOptions()), request, responseObserver);
    }

    /**
     */
    public void preleva(dispatcher.Empty request,
        io.grpc.stub.StreamObserver<dispatcher.Articolo> responseObserver) {
      asyncUnaryCall(
          getChannel().newCall(getPrelevaMethod(), getCallOptions()), request, responseObserver);
    }
  }

  /**
   */
  public static final class MagazzinoBlockingStub extends io.grpc.stub.AbstractStub<MagazzinoBlockingStub> {
    private MagazzinoBlockingStub(io.grpc.Channel channel) {
      super(channel);
    }

    private MagazzinoBlockingStub(io.grpc.Channel channel,
        io.grpc.CallOptions callOptions) {
      super(channel, callOptions);
    }

    @java.lang.Override
    protected MagazzinoBlockingStub build(io.grpc.Channel channel,
        io.grpc.CallOptions callOptions) {
      return new MagazzinoBlockingStub(channel, callOptions);
    }

    /**
     */
    public dispatcher.Empty deposita(dispatcher.Articolo request) {
      return blockingUnaryCall(
          getChannel(), getDepositaMethod(), getCallOptions(), request);
    }

    /**
     */
    public dispatcher.Articolo preleva(dispatcher.Empty request) {
      return blockingUnaryCall(
          getChannel(), getPrelevaMethod(), getCallOptions(), request);
    }
  }

  /**
   */
  public static final class MagazzinoFutureStub extends io.grpc.stub.AbstractStub<MagazzinoFutureStub> {
    private MagazzinoFutureStub(io.grpc.Channel channel) {
      super(channel);
    }

    private MagazzinoFutureStub(io.grpc.Channel channel,
        io.grpc.CallOptions callOptions) {
      super(channel, callOptions);
    }

    @java.lang.Override
    protected MagazzinoFutureStub build(io.grpc.Channel channel,
        io.grpc.CallOptions callOptions) {
      return new MagazzinoFutureStub(channel, callOptions);
    }

    /**
     */
    public com.google.common.util.concurrent.ListenableFuture<dispatcher.Empty> deposita(
        dispatcher.Articolo request) {
      return futureUnaryCall(
          getChannel().newCall(getDepositaMethod(), getCallOptions()), request);
    }

    /**
     */
    public com.google.common.util.concurrent.ListenableFuture<dispatcher.Articolo> preleva(
        dispatcher.Empty request) {
      return futureUnaryCall(
          getChannel().newCall(getPrelevaMethod(), getCallOptions()), request);
    }
  }

  private static final int METHODID_DEPOSITA = 0;
  private static final int METHODID_PRELEVA = 1;

  private static final class MethodHandlers<Req, Resp> implements
      io.grpc.stub.ServerCalls.UnaryMethod<Req, Resp>,
      io.grpc.stub.ServerCalls.ServerStreamingMethod<Req, Resp>,
      io.grpc.stub.ServerCalls.ClientStreamingMethod<Req, Resp>,
      io.grpc.stub.ServerCalls.BidiStreamingMethod<Req, Resp> {
    private final MagazzinoImplBase serviceImpl;
    private final int methodId;

    MethodHandlers(MagazzinoImplBase serviceImpl, int methodId) {
      this.serviceImpl = serviceImpl;
      this.methodId = methodId;
    }

    @java.lang.Override
    @java.lang.SuppressWarnings("unchecked")
    public void invoke(Req request, io.grpc.stub.StreamObserver<Resp> responseObserver) {
      switch (methodId) {
        case METHODID_DEPOSITA:
          serviceImpl.deposita((dispatcher.Articolo) request,
              (io.grpc.stub.StreamObserver<dispatcher.Empty>) responseObserver);
          break;
        case METHODID_PRELEVA:
          serviceImpl.preleva((dispatcher.Empty) request,
              (io.grpc.stub.StreamObserver<dispatcher.Articolo>) responseObserver);
          break;
        default:
          throw new AssertionError();
      }
    }

    @java.lang.Override
    @java.lang.SuppressWarnings("unchecked")
    public io.grpc.stub.StreamObserver<Req> invoke(
        io.grpc.stub.StreamObserver<Resp> responseObserver) {
      switch (methodId) {
        default:
          throw new AssertionError();
      }
    }
  }

  private static abstract class MagazzinoBaseDescriptorSupplier
      implements io.grpc.protobuf.ProtoFileDescriptorSupplier, io.grpc.protobuf.ProtoServiceDescriptorSupplier {
    MagazzinoBaseDescriptorSupplier() {}

    @java.lang.Override
    public com.google.protobuf.Descriptors.FileDescriptor getFileDescriptor() {
      return dispatcher.MagazzinoOuterClass.getDescriptor();
    }

    @java.lang.Override
    public com.google.protobuf.Descriptors.ServiceDescriptor getServiceDescriptor() {
      return getFileDescriptor().findServiceByName("Magazzino");
    }
  }

  private static final class MagazzinoFileDescriptorSupplier
      extends MagazzinoBaseDescriptorSupplier {
    MagazzinoFileDescriptorSupplier() {}
  }

  private static final class MagazzinoMethodDescriptorSupplier
      extends MagazzinoBaseDescriptorSupplier
      implements io.grpc.protobuf.ProtoMethodDescriptorSupplier {
    private final String methodName;

    MagazzinoMethodDescriptorSupplier(String methodName) {
      this.methodName = methodName;
    }

    @java.lang.Override
    public com.google.protobuf.Descriptors.MethodDescriptor getMethodDescriptor() {
      return getServiceDescriptor().findMethodByName(methodName);
    }
  }

  private static volatile io.grpc.ServiceDescriptor serviceDescriptor;

  public static io.grpc.ServiceDescriptor getServiceDescriptor() {
    io.grpc.ServiceDescriptor result = serviceDescriptor;
    if (result == null) {
      synchronized (MagazzinoGrpc.class) {
        result = serviceDescriptor;
        if (result == null) {
          serviceDescriptor = result = io.grpc.ServiceDescriptor.newBuilder(SERVICE_NAME)
              .setSchemaDescriptor(new MagazzinoFileDescriptorSupplier())
              .addMethod(getDepositaMethod())
              .addMethod(getPrelevaMethod())
              .build();
        }
      }
    }
    return result;
  }
}
