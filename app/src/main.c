/*
 * Copyright (c) 2020 Teslabs Engineering S.L.
 * SPDX-License-Identifier: Apache-2.0
 */

#include <zephyr.h>

int main(void)
{
	printk("Hello from application\n");

	while (1) {
		k_sleep(K_MSEC(1000));
	}
}
