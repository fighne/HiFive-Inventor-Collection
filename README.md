# HiFive-Inventor-Collection
This is a collection repository of information on the HiFive Inventor

Source Repositories
- https://github.com/damianburrin/HiFive-PythonSandbox
- https://github.com/fraser125/HiFiveInventor
- https://github.com/tock/tock/tree/master/boards/hifive_inventor

# SiFive related links
- https://www.sifive.com/blog/risc-v-qemu-part-1-privileged-isa-hifive1-virtio
- https://www.sifive.com/blog/risc-v-qemu-part-2-the-risc-v-qemu-port-is-upstream
- 

If I find more I'll add and update here.

YouTube Videos
- https://www.youtube.com/watch?v=6Vy2161Tb48
- 

# Notes on compiler
To compile C/C++ code for the SiFive E31 (an RV32IMAC 32-bit RISC-V core used in the Freedom E310 SoC and HiFive1 board), use the RISC-V GNU Toolchain (riscv64-unknown-elf-gcc or riscv32-unknown-elf-gcc) or Clang/LLVM. [1] (https://www.sifive.com/press/sifive-launches-industrys-first-open-source-risc-v-soc), [2] (https://hackaday.com/2018/06/25/sifive-releases-smaller-lower-power-risc-v-cores/), [3] (https://www.youtube.com/watch?v=sPvMXGFTC2U&t=4), [4] (https://redis-01.surviv.io/risc-v-embedded-development), [5] (https://www.sifive.com/blog/all-aboard-part-1-compiler-args)

Compiler Flags for SiFive E31

The target architecture is defined using three primary compiler flags [-march, -mabi, and -mtune]: [1] (https://www.sifive.com/blog/all-aboard-part-1-compiler-args)
• -march=rv32imac
	• rv32: 32-bit base integer instruction set
	• i: Integer instructions
	• m: Integer multiplication and division
	• a: Atomic instructions
	• c: Compressed instructions (16-bit instructions for smaller code size) [1] (https://gcc.gnu.org/onlinedocs/gcc/RISC-V-Options.html), [2] (https://www.sifive.com/press/sifive-launches-industrys-first-open-source-risc-v-soc)
• -mabi=ilp32
	• Standard 32-bit integer ABI (Integers, Pointers, and Longs are 32-bit). [1] (https://gcc.gnu.org/onlinedocs/gcc/RISC-V-Options.html)
• -mtune=sifive-3-series or -mcpu=sifive-e31 (depending on your GCC/LLVM version)
	• Optimizes scheduling for the 5-stage SiFive E31 pipeline. [1] (https://sifive-china.oss-cn-zhangjiakou.aliyuncs.com/%E5%85%AC%E5%8F%B8%E5%AE%A3%E4%BC%A0%E5%86%8C/company%20brochure%202019%20v2.pdf), [2] (https://gcc.gnu.org/onlinedocs/gcc/RISC-V-Options.html)

Example Compilation Command

bash
riscv64-unknown-elf-gcc -march=rv32imac -mabi=ilp32 -O2 -nostdlib main.c -o main.elf
Use code with caution.

Recommended Development Kits & SDKs

• Freedom E SDK: SiFive provides the SiFive Freedom E SDK which uses the Freedom Metal hardware abstraction library to write portable bare-metal code for the E31 and HiFive1. [1] (https://github.com/sifive/freedom-e-sdk/blob/master/README.md), [2] (https://gitee.com/cnrv-sifive/freedom-e-sdk)
• QEMU Emulation: You can test and prototype E31 binaries without physical hardware using QEMU's built-in qemu-sifive-e31 machine target. [1] (https://github.com/sifive/freedom-e-sdk/blob/master/bsp/qemu-sifive-e31-customer/README.md), [2] (https://gitee.com/cnrv-sifive/freedom-e-sdk)
• Standard Library Options: For microcontrollers with tight memory constraints, using newlib-nano significantly cuts down the binary footprint of standard C library calls like printf. [1] (https://forums.sifive.com/t/gnu-mcu-eclipse/659)
Are you building a bare-metal firmware project from scratch, or trying to port an existing application to a specific board or RTOS (like FreeRTOS)?

# Further Notes
To target the SiFive FE310-G003 SoC (found on boards like the BBC HiFive Inventor) in QEMU, you use the standard 32-bit RISC-V emulator (qemu-system-riscv32) paired with the sifive_e machine configuration. [1] (https://www.sifive.com/blog/risc-v-qemu-part-2-the-risc-v-qemu-port-is-upstream), [2] (https://github.com/tock/tock/blob/master/boards/hifive_inventor/README.md), [3] (https://docs.nxp.com/bundle/GUID-39A0A446-70E5-4ED7-A580-E7508B61A5F1/page/GUID-0C06FA76-0544-4C04-88F4-C90A6EA186DF.html)
Because all iterations of the FE310 family (G000, G002, and G003) feature variations of the underlying SiFive E31 core complex (RV32IMAC), they share the same base memory layout, PLIC (Interrupt Controller), CLINT (Timer), and UART layouts in QEMU. [1] (https://www.sifive.com/blog/risc-v-qemu-part-1-privileged-isa-hifive1-virtio), [2] (https://www.reddit.com/r/RISCV/comments/l7oasn/any_chances_of_a_riscv_dip_mcu/), [3] (https://github.com/sifive/freedom-e-sdk/blob/master/bsp/qemu-sifive-e31-customer/README.md)

1. Direct QEMU Command Line Launch

Run this command from your terminal to target the sifive_e hardware profile:
bash
qemu-system-riscv32 \
  -machine sifive_e \
  -kernel path/to/your/program.elf \
  -nographic \
  -serial stdio
Use code with caution.

2. PlatformIO Configuration (platformio.ini)

If you are developing inside an IDE using PlatformIO Ecosystem, you can configure your testing suite to spin up the QEMU target automatically using this profile: [1] (https://docs.platformio.org/en/latest/plus/debug-tools/qemu.html), [2] (https://community.platformio.org/t/qemu-emulation-of-sifive-board-does-not-update-registers/11523/3)
ini
[env:fe310_g003_emulation]
platform = sifive
framework = freedom-e-sdk
board = e310-arty
debug_tool = qemu
Use code with caution.

3. Debugging over GDB

To pause execution at launch and wait for a GDB debugger socket connections on port 1234, append the -s -S flags to your startup: [1] (https://docs.nxp.com/bundle/GUID-39A0A446-70E5-4ED7-A580-E7508B61A5F1/page/GUID-0C06FA76-0544-4C04-88F4-C90A6EA186DF.html)
bash
qemu-system-riscv32 -machine sifive_e -kernel program.elf -nographic -serial stdio -s -S
Use code with caution.

💡 Notable Differences to Watch For

While QEMU's sifive_e profile perfectly replicates the core components (PLIC, CLINT, UART, and RISC-V Instruction Set Architecture), note that hardware-level specifics on the physical FE310-G003 SoC (such as expanded 64 KB SRAM and custom board-specific I2C sensors) may not have strict device-level models implemented out-of-the-box in upstream QEMU. Ensure your embedded application boots via DTIM / RAM layout variants in your linker script if flash memory mapping causes issues. [1] (https://www.eevblog.com/forum/microcontrollers/is-the-sifive-fe310-a-toy/), [2] (https://github.com/sifive/freedom-e-sdk/blob/master/bsp/qemu-sifive-e31-customer/README.md), [3] (https://www.sifive.com/blog/risc-v-qemu-part-2-the-risc-v-qemu-port-is-upstream)
Are you compiling your project using the SiFive Freedom E SDK or a custom build system? Let me know if you need help modifying your linker script (.ld) to line up with QEMU's memory boundaries.
