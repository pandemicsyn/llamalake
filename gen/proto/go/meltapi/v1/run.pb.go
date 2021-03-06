// Code generated by protoc-gen-go. DO NOT EDIT.
// versions:
// 	protoc-gen-go v1.27.1
// 	protoc        (unknown)
// source: meltapi/v1/run.proto

package meltapiv1

import (
	protoreflect "google.golang.org/protobuf/reflect/protoreflect"
	protoimpl "google.golang.org/protobuf/runtime/protoimpl"
	reflect "reflect"
	sync "sync"
)

const (
	// Verify that this generated code is sufficiently up-to-date.
	_ = protoimpl.EnforceVersion(20 - protoimpl.MinVersion)
	// Verify that runtime/protoimpl is sufficiently up-to-date.
	_ = protoimpl.EnforceVersion(protoimpl.MaxVersion - 20)
)

type SubmitRequest struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	// The blocks to execute e.g. "tap-gitlab some-mapping target-jsonl"
	Blocks string `protobuf:"bytes,1,opt,name=blocks,proto3" json:"blocks,omitempty"`
	// Whether to perform a full refresh
	FullRefresh bool `protobuf:"varint,2,opt,name=full_refresh,json=fullRefresh,proto3" json:"full_refresh,omitempty"`
	// Whether to force a run even if a job with the same ID is already running
	Force bool `protobuf:"varint,3,opt,name=force,proto3" json:"force,omitempty"`
}

func (x *SubmitRequest) Reset() {
	*x = SubmitRequest{}
	if protoimpl.UnsafeEnabled {
		mi := &file_meltapi_v1_run_proto_msgTypes[0]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *SubmitRequest) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*SubmitRequest) ProtoMessage() {}

func (x *SubmitRequest) ProtoReflect() protoreflect.Message {
	mi := &file_meltapi_v1_run_proto_msgTypes[0]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use SubmitRequest.ProtoReflect.Descriptor instead.
func (*SubmitRequest) Descriptor() ([]byte, []int) {
	return file_meltapi_v1_run_proto_rawDescGZIP(), []int{0}
}

func (x *SubmitRequest) GetBlocks() string {
	if x != nil {
		return x.Blocks
	}
	return ""
}

func (x *SubmitRequest) GetFullRefresh() bool {
	if x != nil {
		return x.FullRefresh
	}
	return false
}

func (x *SubmitRequest) GetForce() bool {
	if x != nil {
		return x.Force
	}
	return false
}

type SubmitResponse struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	Jobs []*Job `protobuf:"bytes,2,rep,name=jobs,proto3" json:"jobs,omitempty"`
}

func (x *SubmitResponse) Reset() {
	*x = SubmitResponse{}
	if protoimpl.UnsafeEnabled {
		mi := &file_meltapi_v1_run_proto_msgTypes[1]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *SubmitResponse) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*SubmitResponse) ProtoMessage() {}

func (x *SubmitResponse) ProtoReflect() protoreflect.Message {
	mi := &file_meltapi_v1_run_proto_msgTypes[1]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use SubmitResponse.ProtoReflect.Descriptor instead.
func (*SubmitResponse) Descriptor() ([]byte, []int) {
	return file_meltapi_v1_run_proto_rawDescGZIP(), []int{1}
}

func (x *SubmitResponse) GetJobs() []*Job {
	if x != nil {
		return x.Jobs
	}
	return nil
}

type Job struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	Id    int64  `protobuf:"varint,1,opt,name=id,proto3" json:"id,omitempty"`
	JobId string `protobuf:"bytes,2,opt,name=job_id,json=jobId,proto3" json:"job_id,omitempty"`
	State string `protobuf:"bytes,3,opt,name=state,proto3" json:"state,omitempty"`
}

func (x *Job) Reset() {
	*x = Job{}
	if protoimpl.UnsafeEnabled {
		mi := &file_meltapi_v1_run_proto_msgTypes[2]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *Job) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*Job) ProtoMessage() {}

func (x *Job) ProtoReflect() protoreflect.Message {
	mi := &file_meltapi_v1_run_proto_msgTypes[2]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use Job.ProtoReflect.Descriptor instead.
func (*Job) Descriptor() ([]byte, []int) {
	return file_meltapi_v1_run_proto_rawDescGZIP(), []int{2}
}

func (x *Job) GetId() int64 {
	if x != nil {
		return x.Id
	}
	return 0
}

func (x *Job) GetJobId() string {
	if x != nil {
		return x.JobId
	}
	return ""
}

func (x *Job) GetState() string {
	if x != nil {
		return x.State
	}
	return ""
}

var File_meltapi_v1_run_proto protoreflect.FileDescriptor

var file_meltapi_v1_run_proto_rawDesc = []byte{
	0x0a, 0x14, 0x6d, 0x65, 0x6c, 0x74, 0x61, 0x70, 0x69, 0x2f, 0x76, 0x31, 0x2f, 0x72, 0x75, 0x6e,
	0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x12, 0x0a, 0x6d, 0x65, 0x6c, 0x74, 0x61, 0x70, 0x69, 0x2e,
	0x76, 0x31, 0x22, 0x60, 0x0a, 0x0d, 0x53, 0x75, 0x62, 0x6d, 0x69, 0x74, 0x52, 0x65, 0x71, 0x75,
	0x65, 0x73, 0x74, 0x12, 0x16, 0x0a, 0x06, 0x62, 0x6c, 0x6f, 0x63, 0x6b, 0x73, 0x18, 0x01, 0x20,
	0x01, 0x28, 0x09, 0x52, 0x06, 0x62, 0x6c, 0x6f, 0x63, 0x6b, 0x73, 0x12, 0x21, 0x0a, 0x0c, 0x66,
	0x75, 0x6c, 0x6c, 0x5f, 0x72, 0x65, 0x66, 0x72, 0x65, 0x73, 0x68, 0x18, 0x02, 0x20, 0x01, 0x28,
	0x08, 0x52, 0x0b, 0x66, 0x75, 0x6c, 0x6c, 0x52, 0x65, 0x66, 0x72, 0x65, 0x73, 0x68, 0x12, 0x14,
	0x0a, 0x05, 0x66, 0x6f, 0x72, 0x63, 0x65, 0x18, 0x03, 0x20, 0x01, 0x28, 0x08, 0x52, 0x05, 0x66,
	0x6f, 0x72, 0x63, 0x65, 0x22, 0x35, 0x0a, 0x0e, 0x53, 0x75, 0x62, 0x6d, 0x69, 0x74, 0x52, 0x65,
	0x73, 0x70, 0x6f, 0x6e, 0x73, 0x65, 0x12, 0x23, 0x0a, 0x04, 0x6a, 0x6f, 0x62, 0x73, 0x18, 0x02,
	0x20, 0x03, 0x28, 0x0b, 0x32, 0x0f, 0x2e, 0x6d, 0x65, 0x6c, 0x74, 0x61, 0x70, 0x69, 0x2e, 0x76,
	0x31, 0x2e, 0x4a, 0x6f, 0x62, 0x52, 0x04, 0x6a, 0x6f, 0x62, 0x73, 0x22, 0x42, 0x0a, 0x03, 0x4a,
	0x6f, 0x62, 0x12, 0x0e, 0x0a, 0x02, 0x69, 0x64, 0x18, 0x01, 0x20, 0x01, 0x28, 0x03, 0x52, 0x02,
	0x69, 0x64, 0x12, 0x15, 0x0a, 0x06, 0x6a, 0x6f, 0x62, 0x5f, 0x69, 0x64, 0x18, 0x02, 0x20, 0x01,
	0x28, 0x09, 0x52, 0x05, 0x6a, 0x6f, 0x62, 0x49, 0x64, 0x12, 0x14, 0x0a, 0x05, 0x73, 0x74, 0x61,
	0x74, 0x65, 0x18, 0x03, 0x20, 0x01, 0x28, 0x09, 0x52, 0x05, 0x73, 0x74, 0x61, 0x74, 0x65, 0x32,
	0x4f, 0x0a, 0x0a, 0x52, 0x75, 0x6e, 0x53, 0x65, 0x72, 0x76, 0x69, 0x63, 0x65, 0x12, 0x41, 0x0a,
	0x06, 0x53, 0x75, 0x62, 0x6d, 0x69, 0x74, 0x12, 0x19, 0x2e, 0x6d, 0x65, 0x6c, 0x74, 0x61, 0x70,
	0x69, 0x2e, 0x76, 0x31, 0x2e, 0x53, 0x75, 0x62, 0x6d, 0x69, 0x74, 0x52, 0x65, 0x71, 0x75, 0x65,
	0x73, 0x74, 0x1a, 0x1a, 0x2e, 0x6d, 0x65, 0x6c, 0x74, 0x61, 0x70, 0x69, 0x2e, 0x76, 0x31, 0x2e,
	0x53, 0x75, 0x62, 0x6d, 0x69, 0x74, 0x52, 0x65, 0x73, 0x70, 0x6f, 0x6e, 0x73, 0x65, 0x22, 0x00,
	0x42, 0xa7, 0x01, 0x0a, 0x0e, 0x63, 0x6f, 0x6d, 0x2e, 0x6d, 0x65, 0x6c, 0x74, 0x61, 0x70, 0x69,
	0x2e, 0x76, 0x31, 0x42, 0x08, 0x52, 0x75, 0x6e, 0x50, 0x72, 0x6f, 0x74, 0x6f, 0x50, 0x01, 0x5a,
	0x42, 0x67, 0x69, 0x74, 0x6c, 0x61, 0x62, 0x2e, 0x63, 0x6f, 0x6d, 0x2f, 0x70, 0x61, 0x6e, 0x64,
	0x65, 0x6d, 0x69, 0x63, 0x73, 0x79, 0x6e, 0x2f, 0x6c, 0x6c, 0x61, 0x6d, 0x61, 0x6c, 0x61, 0x6b,
	0x65, 0x2f, 0x67, 0x65, 0x6e, 0x2f, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x2f, 0x67, 0x6f, 0x2f, 0x6d,
	0x65, 0x6c, 0x74, 0x61, 0x70, 0x69, 0x2f, 0x76, 0x31, 0x3b, 0x6d, 0x65, 0x6c, 0x74, 0x61, 0x70,
	0x69, 0x76, 0x31, 0xa2, 0x02, 0x03, 0x4d, 0x58, 0x58, 0xaa, 0x02, 0x0a, 0x4d, 0x65, 0x6c, 0x74,
	0x61, 0x70, 0x69, 0x2e, 0x56, 0x31, 0xca, 0x02, 0x0a, 0x4d, 0x65, 0x6c, 0x74, 0x61, 0x70, 0x69,
	0x5c, 0x56, 0x31, 0xe2, 0x02, 0x16, 0x4d, 0x65, 0x6c, 0x74, 0x61, 0x70, 0x69, 0x5c, 0x56, 0x31,
	0x5c, 0x47, 0x50, 0x42, 0x4d, 0x65, 0x74, 0x61, 0x64, 0x61, 0x74, 0x61, 0xea, 0x02, 0x0b, 0x4d,
	0x65, 0x6c, 0x74, 0x61, 0x70, 0x69, 0x3a, 0x3a, 0x56, 0x31, 0x62, 0x06, 0x70, 0x72, 0x6f, 0x74,
	0x6f, 0x33,
}

var (
	file_meltapi_v1_run_proto_rawDescOnce sync.Once
	file_meltapi_v1_run_proto_rawDescData = file_meltapi_v1_run_proto_rawDesc
)

func file_meltapi_v1_run_proto_rawDescGZIP() []byte {
	file_meltapi_v1_run_proto_rawDescOnce.Do(func() {
		file_meltapi_v1_run_proto_rawDescData = protoimpl.X.CompressGZIP(file_meltapi_v1_run_proto_rawDescData)
	})
	return file_meltapi_v1_run_proto_rawDescData
}

var file_meltapi_v1_run_proto_msgTypes = make([]protoimpl.MessageInfo, 3)
var file_meltapi_v1_run_proto_goTypes = []interface{}{
	(*SubmitRequest)(nil),  // 0: meltapi.v1.SubmitRequest
	(*SubmitResponse)(nil), // 1: meltapi.v1.SubmitResponse
	(*Job)(nil),            // 2: meltapi.v1.Job
}
var file_meltapi_v1_run_proto_depIdxs = []int32{
	2, // 0: meltapi.v1.SubmitResponse.jobs:type_name -> meltapi.v1.Job
	0, // 1: meltapi.v1.RunService.Submit:input_type -> meltapi.v1.SubmitRequest
	1, // 2: meltapi.v1.RunService.Submit:output_type -> meltapi.v1.SubmitResponse
	2, // [2:3] is the sub-list for method output_type
	1, // [1:2] is the sub-list for method input_type
	1, // [1:1] is the sub-list for extension type_name
	1, // [1:1] is the sub-list for extension extendee
	0, // [0:1] is the sub-list for field type_name
}

func init() { file_meltapi_v1_run_proto_init() }
func file_meltapi_v1_run_proto_init() {
	if File_meltapi_v1_run_proto != nil {
		return
	}
	if !protoimpl.UnsafeEnabled {
		file_meltapi_v1_run_proto_msgTypes[0].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*SubmitRequest); i {
			case 0:
				return &v.state
			case 1:
				return &v.sizeCache
			case 2:
				return &v.unknownFields
			default:
				return nil
			}
		}
		file_meltapi_v1_run_proto_msgTypes[1].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*SubmitResponse); i {
			case 0:
				return &v.state
			case 1:
				return &v.sizeCache
			case 2:
				return &v.unknownFields
			default:
				return nil
			}
		}
		file_meltapi_v1_run_proto_msgTypes[2].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*Job); i {
			case 0:
				return &v.state
			case 1:
				return &v.sizeCache
			case 2:
				return &v.unknownFields
			default:
				return nil
			}
		}
	}
	type x struct{}
	out := protoimpl.TypeBuilder{
		File: protoimpl.DescBuilder{
			GoPackagePath: reflect.TypeOf(x{}).PkgPath(),
			RawDescriptor: file_meltapi_v1_run_proto_rawDesc,
			NumEnums:      0,
			NumMessages:   3,
			NumExtensions: 0,
			NumServices:   1,
		},
		GoTypes:           file_meltapi_v1_run_proto_goTypes,
		DependencyIndexes: file_meltapi_v1_run_proto_depIdxs,
		MessageInfos:      file_meltapi_v1_run_proto_msgTypes,
	}.Build()
	File_meltapi_v1_run_proto = out.File
	file_meltapi_v1_run_proto_rawDesc = nil
	file_meltapi_v1_run_proto_goTypes = nil
	file_meltapi_v1_run_proto_depIdxs = nil
}
