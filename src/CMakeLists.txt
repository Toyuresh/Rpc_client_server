
cmake_minimum_required(VERSION 3.0.1)
project(cppdummy CXX)

set(CMAKE_CXX_STANDARD 17)

set (THREADS_PREFER_PTHREAD_FLAG ON)
set( CMAKE_CXX_FLAGS
  "${CMAKE_CXX_FLAGS} -pthread -Wall -Wextra -Wpedantic -Wno-unused-parameter")
  
find_package (Threads)
set (Boost_USE_STATIC_LIBS ON)


include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

find_package(Protobuf REQUIRED)

protobuf_generate_cpp(PROTO_SRCS PROTO_HDRS chat.proto)
protobuf_generate_python(PROTO_PYS chat.proto)

add_subdirectory(baseproto)
include_directories(${CMAKE_BINARY_DIR}/baseproto)
link_libraries(baseproto)


add_executable(test  main.cpp  ${PROTO_SRCS} ${PROTO_HDRS})
target_link_libraries(test boost_coroutine)
target_link_libraries(test  protobuf boost_thread boost_system boost_context baseproto)
target_include_directories(test PRIVATE ${CMAKE_BINARY_DIR})
set_target_properties(test PROPERTIES CXX_STANDARD 17)

add_executable(client client.cpp ${PROTO_SRCS} ${PROTO_HDRS})
target_link_libraries(client boost_coroutine)
target_link_libraries(client protobuf boost_thread boost_system boost_context baseproto)
target_include_directories(client PRIVATE ${CMAKE_BINARY_DIR})
set_target_properties(client PROPERTIES CXX_STANDARD 17)

add_custom_target(proto_python ALL DEPENDS ${PROTO_PYS})