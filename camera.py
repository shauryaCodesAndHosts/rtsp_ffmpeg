import os
import subprocess
import time
from datetime import datetime

def create_directory_and_change():
    today_date = datetime.now().strftime('%Y-%m-%d')
    if not os.path.exists(today_date):
        os.makedirs(today_date)
    os.chdir(today_date)

def get_today_date():
    return datetime.now().strftime('%Y-%m-%d')

def run_ffmpeg():
    # ffmpeg_command = [
    #     "ffmpeg", "-hide_banner", "-y", "-rtsp_transport", "udp", "-use_wallclock_as_timestamps", "1",
    #     "-i", "rtsp://shaurya:Annpurna@192.168.29.180:554/stream1", "-vcodec", "copy", "-acodec", "copy",
    #     "-f", "segment", "-reset_timestamps", "1", "-segment_time", "900", "-segment_format", "mkv",
    #     "-segment_atclocktime", "1", "-strftime", "1", "%Y%m%dT%H%M%S.mkv"
    # ]

    ffmpeg_command = [
    "ffmpeg", "-rtsp_transport", "tcp","-stimeout","30000000", "-use_wallclock_as_timestamps", "1",
    "-i", "rtsp://shaurya:Annpurna@192.168.29.180:554/stream1", "-vcodec", "copy", "-acodec", "copy",
    "-f", "segment", "-reset_timestamps", "1", "-segment_time", "900", "-segment_format", "mkv",
    "-segment_atclocktime", "1", "-strftime", "1", "%Y%m%dT%H%M%S.mkv"
    ]


    current_date = get_today_date()
    create_directory_and_change()

    while True:
        try:
            if current_date != get_today_date():
                current_date = get_today_date()
                create_directory_and_change()
            subprocess.run(ffmpeg_command, check=True)
        except subprocess.CalledProcessError as e:
            print(f"ffmpeg process failed with error: {e}. Retrying in 1 minute.")
            time.sleep(60)

if __name__ == "__main__":
    run_ffmpeg()
