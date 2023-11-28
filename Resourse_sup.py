import psutil
import time
import loguru

def monitor_all_processes(threshold_memory_mb=200, interval=1):
    print("Monitoring all processes...")

    try:
        while True:


            # 或許所有進程的訊息
            all_processes = psutil.process_iter(['pid', 'name', 'memory_info'])

            for process in all_processes:
                pid = process.info['pid']
                name = process.info['name']
                memory_info = process.info['memory_info']


                # 記憶體（以MB为單位）
                memory_usage_mb = memory_info.rss / (1024 ** 2)

                loguru.logger.debug(f"PID: {pid}, Name: {name}, Memory Usage: {memory_usage_mb:.2f} MB")
                time.sleep(3)
                # 如果 CPU 使用率超过阈值，进行警告
                if memory_usage_mb > threshold_memory_mb:
                    loguru.logger.error(f"Warning: High memory usage detected for PID {pid} ({name})")

            time.sleep(interval)

    except KeyboardInterrupt:
        loguru.logger.warning("Monitoring stopped.")

if __name__ == "__main__":
    # 設置 記憶體 使用率阈值（MB）
    memory_threshold = 200

    monitor_all_processes(threshold_memory_mb=memory_threshold)
