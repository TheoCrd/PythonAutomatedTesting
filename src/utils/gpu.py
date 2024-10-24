# src/utils/gpu.py
from __future__ import annotations

import cupy as cp


class GPU:
    def __init__(
        self,
        id,
        name,
        total_memory,
        multiprocessor_count,
        clock_rate,
        memory_clock_rate,
        memory_bus_width,
        compute_capability,
    ):
        self.id = id
        self.name = name
        self.total_memory = total_memory
        self.multiprocessor_count = multiprocessor_count
        self.clock_rate = clock_rate
        self.memory_clock_rate = memory_clock_rate
        self.memory_bus_width = memory_bus_width
        self.compute_capability = compute_capability

    def get_info(self):
        return {
            "id": self.id,
            "name": self.name,
            "total_memory": self.total_memory,
            "multiprocessor_count": self.multiprocessor_count,
            "clock_rate": self.clock_rate,
            "memory_clock_rate": self.memory_clock_rate,
            "memory_bus_width": self.memory_bus_width,
            "compute_capability": self.compute_capability,
        }

    def __str__(self):
        return (
            f"GPU {self.id}: {self.name}, {self.total_memory} MB, {self.multiprocessor_count} SM, "
            f"{self.clock_rate} MHz, {self.memory_clock_rate} MHz, {self.memory_bus_width} bit bus, "
            f"CC {self.compute_capability}"
        )


def get_gpu_info():
    try:
        num_gpus = cp.cuda.runtime.getDeviceCount()
    except cp.cuda.runtime.CUDARuntimeError as e:
        print(f"CUDA Runtime Error: {e}")
        return []
    num_gpus = cp.cuda.runtime.getDeviceCount()

    gpu_info = []

    for i in range(num_gpus):
        props = cp.cuda.runtime.getDeviceProperties(i)
        gpu = GPU(
            id=i,
            name=(
                props["name"].decode("utf-8")
                if isinstance(props["name"], bytes)
                else props["name"]
            ),
            total_memory=props["totalGlobalMem"]
            / (1024**2),  # Convert bytes to MB
            multiprocessor_count=props["multiProcessorCount"],
            clock_rate=props["clockRate"] / 1000,  # Convert kHz to MHz
            memory_clock_rate=props["memoryClockRate"]
            / 1000,  # Convert kHz to MHz
            memory_bus_width=props["memoryBusWidth"],
            compute_capability=f"{props['major']}.{props['minor']}",
        )
        gpu_info.append(gpu)

    return gpu_info


def print_gpu_info():
    for gpu in get_gpu_info():
        print(gpu)
