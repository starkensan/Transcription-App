import whisper
import tkinter as tk
from tkinter import filedialog, scrolledtext, messagebox
import threading


def whisper_init(model_size):
    global model
    model = whisper.load_model(model_size)

def transcribe_audio(filepath, output_box, status_label):
    try:
        status_label.config(text="文字起こし中...")
        output_box.delete("1.0", tk.END)
        result = model.transcribe(filepath, fp16=False)
        output_box.insert(tk.END, result["text"])
        status_label.config(text="文字起こし完了")
    except Exception as e:
        status_label.config(text="エラーが発生しました")
        messagebox.showerror("エラー", f"エラーが発生しました:\n{str(e)}")

def browse_file(output_box, status_label):
    filepath = filedialog.askopenfilename(
        filetypes=[("音声ファイル", "*.mp3 *.wav *.m4a *.mp4")]
    )
    if filepath:
        threading.Thread(target=transcribe_audio, args=(filepath, output_box, status_label)).start()

def copy_to_clipboard(output_box, root):
    text = output_box.get("1.0", tk.END).strip()
    if text:
        root.clipboard_clear()
        root.clipboard_append(text)
        messagebox.showinfo("コピー完了", "文字起こし結果をクリップボードにコピーしました。")
    else:
        messagebox.showwarning("空のテキスト", "コピーする内容がありません。")

# GUIの構築
def main():
    whisper_init("base")

    root = tk.Tk()
    root.title("Whisper 音声文字起こしアプリ")
    root.geometry("600x450")

    label = tk.Label(root, text="MP3ファイルを選択してください")
    label.pack(pady=5)

    status_label = tk.Label(root, text="", fg="blue")
    status_label.pack(pady=5)

    text_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=70, height=18)
    text_area.pack(padx=10, pady=5)

    button_frame = tk.Frame(root)
    button_frame.pack(pady=10)

    transcribe_button = tk.Button(
        button_frame, text="ファイルを選択して文字起こし",
        command=lambda: browse_file(text_area, status_label)
    )
    transcribe_button.grid(row=0, column=0, padx=10)

    copy_button = tk.Button(
        button_frame, text="コピーする",
        command=lambda: copy_to_clipboard(text_area, root)
    )
    copy_button.grid(row=0, column=1, padx=10)

    root.mainloop()

if __name__ == "__main__":
    main()
