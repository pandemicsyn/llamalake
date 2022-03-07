// Code generated by protoc-gen-go-grpc. DO NOT EDIT.
// versions:
// - protoc-gen-go-grpc v1.2.0
// - protoc             (unknown)
// source: meltapi/v1/run.proto

package meltapiv1

import (
	context "context"
	grpc "google.golang.org/grpc"
	codes "google.golang.org/grpc/codes"
	status "google.golang.org/grpc/status"
)

// This is a compile-time assertion to ensure that this generated file
// is compatible with the grpc package it is being compiled against.
// Requires gRPC-Go v1.32.0 or later.
const _ = grpc.SupportPackageIsVersion7

// RunServiceClient is the client API for RunService service.
//
// For semantics around ctx use and closing/ending streaming RPCs, please refer to https://pkg.go.dev/google.golang.org/grpc/?tab=doc#ClientConn.NewStream.
type RunServiceClient interface {
	Submit(ctx context.Context, in *SubmitRequest, opts ...grpc.CallOption) (*SubmitResponse, error)
}

type runServiceClient struct {
	cc grpc.ClientConnInterface
}

func NewRunServiceClient(cc grpc.ClientConnInterface) RunServiceClient {
	return &runServiceClient{cc}
}

func (c *runServiceClient) Submit(ctx context.Context, in *SubmitRequest, opts ...grpc.CallOption) (*SubmitResponse, error) {
	out := new(SubmitResponse)
	err := c.cc.Invoke(ctx, "/meltapi.v1.RunService/Submit", in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

// RunServiceServer is the server API for RunService service.
// All implementations should embed UnimplementedRunServiceServer
// for forward compatibility
type RunServiceServer interface {
	Submit(context.Context, *SubmitRequest) (*SubmitResponse, error)
}

// UnimplementedRunServiceServer should be embedded to have forward compatible implementations.
type UnimplementedRunServiceServer struct {
}

func (UnimplementedRunServiceServer) Submit(context.Context, *SubmitRequest) (*SubmitResponse, error) {
	return nil, status.Errorf(codes.Unimplemented, "method Submit not implemented")
}

// UnsafeRunServiceServer may be embedded to opt out of forward compatibility for this service.
// Use of this interface is not recommended, as added methods to RunServiceServer will
// result in compilation errors.
type UnsafeRunServiceServer interface {
	mustEmbedUnimplementedRunServiceServer()
}

func RegisterRunServiceServer(s grpc.ServiceRegistrar, srv RunServiceServer) {
	s.RegisterService(&RunService_ServiceDesc, srv)
}

func _RunService_Submit_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(SubmitRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(RunServiceServer).Submit(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: "/meltapi.v1.RunService/Submit",
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(RunServiceServer).Submit(ctx, req.(*SubmitRequest))
	}
	return interceptor(ctx, in, info, handler)
}

// RunService_ServiceDesc is the grpc.ServiceDesc for RunService service.
// It's only intended for direct use with grpc.RegisterService,
// and not to be introspected or modified (even as a copy)
var RunService_ServiceDesc = grpc.ServiceDesc{
	ServiceName: "meltapi.v1.RunService",
	HandlerType: (*RunServiceServer)(nil),
	Methods: []grpc.MethodDesc{
		{
			MethodName: "Submit",
			Handler:    _RunService_Submit_Handler,
		},
	},
	Streams:  []grpc.StreamDesc{},
	Metadata: "meltapi/v1/run.proto",
}
