#-------------------------------------------------------------------------------
# Application firmware
#
# Copyright (c) 2020 Teslabs Engineering S.L.
# SPDX-License-Identifier: Apache-2.0

if(NOT DEFINED BOARD_ROOT)
  set(BOARD_ROOT ${CMAKE_SOURCE_DIR})
endif()

if(NOT DEFINED BOARD)
  set(BOARD "app_board")
endif()

cmake_minimum_required(VERSION 3.13.1)
find_package(Zephyr REQUIRED HINTS $ENV{ZEPHYR_BASE})

project(app LANGUAGES C VERSION 1.0.0)

#-------------------------------------------------------------------------------
# Options

set(CMAKE_EXPORT_COMPILE_COMMANDS ON)

#-------------------------------------------------------------------------------
# Application

zephyr_include_directories(include)

add_subdirectory(src)
