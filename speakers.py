import config
from GPT_SoVITS.TTS_infer_pack.TTS import TTS, TTS_Config


def create_config(t2s_weights_path, vits_weights_path):
    tts_config = TTS_Config()
    tts_config.device = "cuda"
    tts_config.is_half = True
    tts_config.version = "v2"
    tts_config.bert_base_path = config.bert_path
    tts_config.cnhuhbert_base_path = config.cnhubert_path
    tts_config.sampling_rate = 16000
    tts_config.t2s_weights_path = t2s_weights_path
    tts_config.vits_weights_path = vits_weights_path
    return tts_config


v2_languages: list = ["auto", "auto_yue", "en", "zh", "ja", "yue", "ko", "all_zh", "all_ja", "all_yue", "all_ko"]

tts_configs: dict = {
    "kele": {
        "config": create_config("./speakers/kele/kele-e20.ckpt", "./speakers/kele/kele_e12_s264.pth"),
        "ref_audio_path": "./speakers/kele/sample.wav",
        "prompt_text": "电机每分钟的转速呢，高达一千五到一千八百转，油脂分离率呢高达百分之八十以上。电机功率是一个三百多瓦的电机大功率。",
        "fragment_interval": 0.02,
        "seed": 522029860
    },
    "lulu": {
        "config": create_config("./speakers/lulu/lulu-e20.ckpt", "./speakers/lulu/lulu_e12_s144.pth"),
        "ref_audio_path": "./speakers/lulu/sample.wav",
        "prompt_text": "帮你抢先占领我们的公共烟管，做到的是不用调档的智能循环增压，所以非常节能非常方便。",
        "fragment_interval": 0.01,
        "seed": 3421734686
    },
    "rose": {
        "config": create_config("./speakers/rose/rose-e20.ckpt", "./speakers/rose/rose_e12_s156.pth"),
        "ref_audio_path": "./speakers/rose/sample.wav",
        "prompt_text": "它的风压有一千，静压一千二，能够帮助你呢，率先抢占烟道冲顶直排，排烟顺畅，笼烟干净。",
        "fragment_interval": 0.01,
        "seed": 912000325
    }
}

tts_pipelines: dict = {}


def get_tts_pipeline(speaker_name):
    global tts_pipelines
    if speaker_name not in tts_pipelines:
        tts_pipelines[speaker_name] = TTS(tts_configs[speaker_name]["config"])

    return tts_pipelines[speaker_name]
