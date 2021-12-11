# Protobuf example

To generate the python code from the proto file

``` bash
python -m grpc_tools.protoc -I protobufs --python_out=recommendations --grpc_python_out=recommendations protobufs/recommendations.proto
```

### Reference

https://realpython.com/python-microservices-grpc/
