# partially done
import time

# User input
window_size = int(input("Enter the number of frames that can be sent before needing an ACK: "))
total_frames = int(input("Enter the total number of frames to send: "))
timeout = int(input("Enter the timeout duration (in seconds): "))

# Frame sending function
def send_frame(frame_number):
    print(f"Sending frame {frame_number}...")
    success = input("Was the frame sent successfully? (True/False): ").strip().lower()
    return success == 'true'

# Simulate receiving ACKs with user input
def receive_ack(expected_frame):
    print(f"Waiting for ACK for frame {expected_frame}...")
    ack = input(f"Enter {expected_frame} if ACK received, or 'None' if lost: ").strip()
    if ack.lower() == 'none':
        return None
    return int(ack)

# Selective Repeat ARQ Implementation
def selective_repeat_arq():
    base = 0
    next_frame_to_send = 0
    ack_received = [-1] * total_frames  # -1 indicates not acknowledged
    sent_status = [False] * total_frames  # Tracks whether a frame was successfully sent

    while base < total_frames:
        # Send all frames in the current window
        for i in range(base, min(base + window_size, total_frames)):
            if not sent_status[i]:  # Only send unsent or lost frames
                if send_frame(i):
                    print(f"Frame {i} sent successfully.")
                    sent_status[i] = True
                else:
                    print(f"Frame {i} lost. Will retry.")

        # Check for ACKs only for successfully sent frames
        for i in range(base, min(base + window_size, total_frames)):
            if sent_status[i] and ack_received[i] == -1:  # Check only sent and unacknowledged frames
                ack = receive_ack(i)
                if ack is not None and ack == i:
                    print(f"Received ACK for frame {i}.")
                    ack_received[i] = 1  # Mark as acknowledged
                else:   
                    print(f"ACK lost for frame {i}. Frame will be resent.")

        # Slide the window
        while base < total_frames and ack_received[base] == 1:
            base += 1

if __name__ == "__main__":
    selective_repeat_arq()
