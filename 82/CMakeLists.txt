cmake_minimum_required(VERSION 3.5)
project(82)

set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++11")

set(SOURCE_FILES
    82.c
    82.h)

add_executable(82 ${SOURCE_FILES})