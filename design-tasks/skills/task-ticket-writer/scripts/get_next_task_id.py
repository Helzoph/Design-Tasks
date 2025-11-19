#!/usr/bin/env python3
"""
获取下一个任务ID

这个脚本会扫描指定目录下的所有任务文件，找出最大的ID并返回下一个ID。
支持命令行参数指定目录路径，默认扫描 docs/tasks 目录。
"""

import os
import re
import sys

def get_next_task_id(tasks_dir: str = "docs/tasks") -> str:
    """
    获取下一个任务ID

    Args:
        tasks_dir: 任务文件目录路径

    Returns:
        下一个任务ID字符串（如 "002"）

    Raises:
        FileNotFoundError: 如果任务目录不存在
    """
    if not os.path.exists(tasks_dir):
        print("001")
        return "001"

    max_id = 0
    task_id_pattern = re.compile(r'^(\d+)-.*\.md$')

    for filename in os.listdir(tasks_dir):
        match = task_id_pattern.match(filename)
        if match:
            task_id = int(match.group(1))
            max_id = max(max_id, task_id)

    next_id = max_id + 1
    formatted_id = f"{next_id:03d}"

    print(formatted_id)
    return formatted_id


if __name__ == "__main__":
    try:
        # 支持命令行参数指定目录路径
        tasks_dir = sys.argv[1] if len(sys.argv) > 1 else "docs/tasks"
        _ = get_next_task_id(tasks_dir)
    except Exception as e:
        print(f"Error: {e}")
        print("001")
