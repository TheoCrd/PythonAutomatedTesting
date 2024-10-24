from __future__ import annotations

import cupy as cp

from utils.gpu import get_gpu_info
from utils.gpu import GPU
from utils.gpu import print_gpu_info


def test_gpu_initialization(mock_gpu):
    """Test that the GPU class initializes"""
    gpu = mock_gpu
    assert gpu.id == 0
    assert gpu.name == "Mock GPU"
    assert gpu.total_memory == 8192
    assert gpu.multiprocessor_count == 16
    assert gpu.clock_rate == 1500
    assert gpu.memory_clock_rate == 7000
    assert gpu.memory_bus_width == 256
    assert gpu.compute_capability == "7.5"


def test_gpu_str(mock_gpu):
    """Test that the GPU class returns the correct string representation"""
    gpu = mock_gpu
    expected_str = "GPU 0: Mock GPU, 8192 MB, 16 SM, 1500 MHz, 7000 MHz, 256 bit bus, CC 7.5"
    assert str(gpu) == expected_str


def test_get_info(mock_gpu):
    """Test that get_info returns the correct GPU information"""
    gpu = mock_gpu
    info = gpu.get_info()
    assert info == {
        "id": 0,
        "name": "Mock GPU",
        "total_memory": 8192,
        "multiprocessor_count": 16,
        "clock_rate": 1500,
        "memory_clock_rate": 7000,
        "memory_bus_width": 256,
        "compute_capability": "7.5",
    }


def test_get_gpu_info(mocker):
    """Test that get_gpu_info returns the correct GPU information"""
    mocker.patch("utils.gpu.cp.cuda.runtime.getDeviceCount", return_value=1)
    mocker.patch(
        "utils.gpu.cp.cuda.runtime.getDeviceProperties",
        return_value={
            "name": b"Mock GPU",
            "totalGlobalMem": 8589934592,  # 8 GB in bytes
            "multiProcessorCount": 16,
            "clockRate": 1500000,  # 1500 MHz in kHz
            "memoryClockRate": 7000000,  # 7000 MHz in kHz
            "memoryBusWidth": 256,
            "major": 7,
            "minor": 5,
        },
    )

    info = get_gpu_info()
    assert len(info) == 1
    gpu = info[0]
    assert gpu.id == 0
    assert gpu.name == "Mock GPU"
    assert gpu.total_memory == 8192  # 8 GB in MB
    assert gpu.multiprocessor_count == 16
    assert gpu.clock_rate == 1500  # MHz
    assert gpu.memory_clock_rate == 7000  # MHz
    assert gpu.memory_bus_width == 256
    assert gpu.compute_capability == "7.5"


def test_get_gpu_info_no_gpus(mocker):
    """Test that get_gpu_info returns an empty list when no GPUs are found"""
    mocker.patch("utils.gpu.cp.cuda.runtime.getDeviceCount", return_value=0)
    info = get_gpu_info()
    assert len(info) == 0


def test_get_gpu_info_cuda_error(mocker):
    """Test that get_gpu_info returns an empty list when a CUDA error occurs"""
    mocker.patch(
        "utils.gpu.cp.cuda.runtime.getDeviceCount",
        side_effect=cp.cuda.runtime.CUDARuntimeError(1),
    )
    info = get_gpu_info()
    assert len(info) == 0


def test_print_gpu_info(mocker, capfd):
    # Mock the get_gpu_info function to return a known set of GPUs
    mocker.patch(
        "utils.gpu.get_gpu_info",
        return_value=[
            GPU(
                id=0,
                name="Mock GPU",
                total_memory=8192,
                multiprocessor_count=16,
                clock_rate=1500,
                memory_clock_rate=7000,
                memory_bus_width=256,
                compute_capability="7.5",
            )
        ],
    )

    # Call the function to print GPU info
    print_gpu_info()

    # Capture the output
    captured = capfd.readouterr()

    # Verify the output
    expected_output = "GPU 0: Mock GPU, 8192 MB, 16 SM, 1500 MHz, 7000 MHz, 256 bit bus, CC 7.5\n"
    assert captured.out == expected_output
