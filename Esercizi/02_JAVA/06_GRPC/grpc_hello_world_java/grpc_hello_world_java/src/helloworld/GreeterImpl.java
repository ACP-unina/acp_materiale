package helloworld;


import io.grpc.stub.StreamObserver;

public class GreeterImpl extends GreeterGrpc.GreeterImplBase {
    @Override
    public void sayHello(HelloRequest req, StreamObserver<HelloReply> responseObserver) {
        System.out.println("[SERVER JAVA GRPC] Invoked sayHello");
        HelloReply reply = HelloReply.newBuilder().setMessage("Hello " + req.getName()).build();
        System.out.println("[SERVER JAVA GRPC] Set reply and send...");
        responseObserver.onNext(reply);
        responseObserver.onCompleted();
    }
}
    