"""UI strings for VibeVoice community Gradio demo (English / Simplified Chinese).

Used by ``gradio_demo.py`` when ``--zh`` is passed to show a Chinese primary UI.
"""


def ui_strings(lang: str) -> dict[str, str]:
    """Return label/markdown strings for the given language code."""
    use_zh = lang.lower().startswith("zh")
    if not use_zh:
        return _EN
    return _ZH


_EN = {
    "window_title": "VibeVoice Community — Multi-speaker TTS",
    "header_html": """
        <div style="text-align:center"><h1>VibeVoice</h1>
        <p>Expressive long-form conversational speech · voice reference / cloning in Advanced</p></div>
        """,
    "model_info_label": "Current Model",
    "podcast_settings": "### **Podcast Settings**",
    "num_speakers": "Number of Speakers",
    "speaker_selection": "### 🎭 **Speaker Selection**",
    "speaker_n": "Speaker {}",
    "advanced_settings": "### ⚙️ **Advanced Settings**",
    "generation_parameters": "Generation Parameters",
    "cfg_scale": "CFG Scale (Guidance Strength)",
    "inference_steps": "Inference Steps",
    "seed": "Seed (-1 = random)",
    "disable_voice_cloning": "Disable voice cloning (skip conditioning voice prompts)",
    "disable_voice_cloning_info": "When enabled, sets is_prefill=False so the model ignores provided speaker audio.",
    "custom_voice_title": "Upload Custom Voice (Clone)",
    "custom_voice_hint": "Upload a WAV/MP3 recording (5–30 s recommended). It will be saved as a new speaker preset.",
    "custom_voice_upload": "Reference Audio",
    "custom_voice_name": "Speaker Name",
    "custom_voice_name_placeholder": "e.g. my-voice",
    "custom_voice_add": "Add Speaker",
    "custom_voice_error_empty": "Please provide both an audio file and a speaker name.",
    "script_input": "### 📝 **Script Input**",
    "conversation_script": "Conversation Script",
    "script_placeholder": """Enter your podcast script here. You can format it as:

Speaker 1: Welcome to our podcast today!
Speaker 2: Thanks for having me. I'm excited to discuss...

Or paste text directly and it will auto-assign speakers.""",
    "random_example": "🎲 Random Example",
    "generate": "🚀 Generate Podcast",
    "stop": "🛑 Stop Generation",
    "streaming_status_html": """
                    <div style="background: linear-gradient(135deg, #dcfce7 0%, #bbf7d0 100%);
                                border: 1px solid rgba(34, 197, 94, 0.3);
                                border-radius: 8px;
                                padding: 0.75rem;
                                margin: 0.5rem 0;
                                text-align: center;
                                font-size: 0.9rem;
                                color: #166534;">
                        <span class="streaming-indicator"></span>
                        <strong>LIVE STREAMING</strong> - Audio is being generated in real-time
                    </div>
                    """,
    "generated_podcast": "### 🎵 **Generated Podcast**",
    "streaming_audio": "Streaming Audio (Real-time)",
    "complete_audio": "Complete Podcast (Download after generation)",
    "stream_hints": """
                *💡 **Streaming**: Audio plays as it's being generated (may have slight pauses)
                *💡 **Complete Audio**: Will appear below after generation finishes*
                """,
    "generation_log": "Generation Log",
    "usage_tips": """
        ### 💡 **Usage Tips**

        - Click **🚀 Generate Podcast** to start audio generation
        - **Live Streaming** tab shows audio as it's generated (may have slight pauses)
        - **Complete Audio** tab provides the full, uninterrupted podcast after generation
        - During generation, you can click **🛑 Stop Generation** to interrupt the process
        - The streaming indicator shows real-time generation progress
        """,
    "example_scripts": "### 📚 **Example Scripts**",
    "examples_label": "Try these example scripts:",
    "risks": """
## Risks and limitations

While efforts have been made to optimize it through various techniques, it may still produce outputs that are unexpected, biased, or inaccurate. VibeVoice inherits any biases, errors, or omissions produced by its base model (specifically, Qwen2.5 1.5b in this release).
Potential for Deepfakes and Disinformation: High-quality synthetic speech can be misused to create convincing fake audio content for impersonation, fraud, or spreading disinformation. Users must ensure transcripts are reliable, check content accuracy, and avoid using generated content in misleading ways. Users are expected to use the generated content and to deploy the models in a lawful manner, in full compliance with all applicable laws and regulations in the relevant jurisdictions. It is best practice to disclose the use of AI when sharing AI-generated content.
            """,
}

_ZH = {
    "window_title": "VibeVoice 社区版 — 多说话人语音合成",
    "header_html": """
        <div style="text-align:center"><h1>VibeVoice 社区版</h1>
        <p>表现力长对话语音合成 · 可在高级设置中关闭「禁用声音克隆」以使用参考音频条件</p></div>
        """,
    "model_info_label": "当前模型",
    "podcast_settings": "### **播客 / 对话设置**",
    "num_speakers": "说话人数量",
    "speaker_selection": "### 🎭 **说话人选择**",
    "speaker_n": "说话人 {}",
    "advanced_settings": "### ⚙️ **高级设置**",
    "generation_parameters": "生成参数",
    "cfg_scale": "CFG 引导强度",
    "inference_steps": "扩散步数",
    "seed": "随机种子（-1 为随机）",
    "disable_voice_cloning": "禁用声音克隆（跳过参考音频条件）",
    "disable_voice_cloning_info": "勾选后 is_prefill=False，模型将忽略提供的说话人参考音频。",
    "custom_voice_title": "上传自定义音色（声音克隆）",
    "custom_voice_hint": "上传一段 WAV/MP3 录音（建议 5–30 秒），将保存为新的说话人预设，随后可在上方下拉框选择。",
    "custom_voice_upload": "参考音频",
    "custom_voice_name": "说话人名称",
    "custom_voice_name_placeholder": "例如 my-voice",
    "custom_voice_add": "添加说话人",
    "custom_voice_error_empty": "请同时提供音频文件和说话人名称。",
    "script_input": "### 📝 **台本输入**",
    "conversation_script": "对话台本",
    "script_placeholder": """在此输入播客或对话台本，例如：

Speaker 1: 欢迎收听本期节目！
Speaker 2: 很高兴来到这里……

也可直接粘贴文本，系统会尽量自动分配说话人。""",
    "random_example": "🎲 随机示例",
    "generate": "🚀 生成语音",
    "stop": "🛑 停止生成",
    "streaming_status_html": """
                    <div style="background: linear-gradient(135deg, #dcfce7 0%, #bbf7d0 100%);
                                border: 1px solid rgba(34, 197, 94, 0.3);
                                border-radius: 8px;
                                padding: 0.75rem;
                                margin: 0.5rem 0;
                                text-align: center;
                                font-size: 0.9rem;
                                color: #166534;">
                        <span class="streaming-indicator"></span>
                        <strong>实时流式输出</strong> — 音频正在生成中
                    </div>
                    """,
    "generated_podcast": "### 🎵 **生成结果**",
    "streaming_audio": "流式音频（实时）",
    "complete_audio": "完整音频（生成结束后可下载）",
    "stream_hints": """
                *💡 **流式**：生成过程中逐段播放（可能有短暂停顿）*
                *💡 **完整音频**：全部生成完成后显示在下方，可下载*
                """,
    "generation_log": "生成日志",
    "usage_tips": """
        ### 💡 **使用说明**

        - 点击 **🚀 生成语音** 开始合成
        - 流式区域会随生成进度更新（可能有短暂停顿）
        - **完整音频** 在整段生成结束后提供，便于下载
        - 生成过程中可点击 **🛑 停止生成** 中断
        - 状态条用于提示当前是否在流式生成
        """,
    "example_scripts": "### 📚 **示例台本**",
    "examples_label": "可尝试以下示例：",
    "risks": """
## 风险与限制

模型输出仍可能出现意外、偏见或不准确。合成语音存在被滥用于伪造身份、欺诈或误导性传播的风险。请确保用途合法合规，对外分享时建议披露使用了 AI 生成内容。
            """,
}
