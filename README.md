# Zephyr Application Boilerplate

This repository contains a Zephyr application boilerplate. While it targets
STM32 based applications, it can be exported to any other setup.

# Getting started

Before getting started, make sure you have a proper Zephyr development
environment. You can follow the official [Getting Started Guide](https://docs.zephyrproject.org/latest/getting_started/index.html).

After cloning the repository first initialize `west` environment:

``` sh
west init -l app
```

Once initialized, you need to make sure Zephyr and its modules are up-to-date:

``` sh
west update
```

At this point you can build the application as usual:

``` sh
west build -s app -b app_board
```

A debug configuration is also provided, you can enable it by running:

``` sh
west build -s app -b app_board -- -DOVERLAY_CONFIG=debug.conf
```

Once you have built the application you can flash it by running:

``` sh
west flash
```

# Tests

You can run tests by executing:

```sh
./zephyr/scripts/sanitycheck -T app/tests
```

You can use regular `sanitycheck` arguments to filter, list, run on device, etc.
