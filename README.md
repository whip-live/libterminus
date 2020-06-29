# Terminus WHIP Library

All-purpose library

## Source tree summary

`messages`: contains `.proto` definitions
`scripts`: contains utility scripts
`terminus`: the library's source code
`tests`: well... tests

## How to compile proto messages

To compile `.proto` definitions first you need to download the compiler at https://github.com/protocolbuffers/protobuf/releases/latest

Once you have installed it ensure it is on the path and run the script `scripts/compile_proto_messages.sh` to generate new definitions.

You can override the command used by defining the `PROTOC` variable:

    $ PROTOC=/home/user/proto/bin/protoc scripts/compile_proto_messages.sh


**NOTE**
The compilation process is not automated and should be performed when the messages definitions are changed.
