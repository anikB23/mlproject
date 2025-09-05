import logging
import os
from datetime import datetime

# Create logs directory (not including the filename)
logs_dir = os.path.join(os.getcwd(), "logs")
os.makedirs(logs_dir, exist_ok=True)

# File name with timestamp
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# Full file path
LOG_FILE_PATH = os.path.join(logs_dir, LOG_FILE)

# Configure logging
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
    encoding="utf-8"
)

#if __name__ == "__main__":
#    logging.info("Logging has started")
#    print(f"✅ Log file created at: {LOG_FILE_PATH}")

