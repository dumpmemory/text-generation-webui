import functools
from collections import OrderedDict

import gradio as gr

loaders_and_params = OrderedDict({
    'llama.cpp': [
        'gpu_layers',
        'threads',
        'threads_batch',
        'batch_size',
        'ctx_size',
        'cache_type',
        'tensor_split',
        'extra_flags',
        'streaming_llm',
        'rope_freq_base',
        'compress_pos_emb',
        'flash_attn',
        'row_split',
        'no_kv_offload',
        'no_mmap',
        'mlock',
        'numa',
        'model_draft',
        'draft_max',
        'gpu_layers_draft',
        'device_draft',
        'ctx_size_draft',
        'speculative_decoding_accordion',
        'vram_info',
    ],
    'Transformers': [
        'gpu_split',
        'cpu_memory',
        'alpha_value',
        'compress_pos_emb',
        'compute_dtype',
        'quant_type',
        'load_in_8bit',
        'load_in_4bit',
        'attn_implementation',
        'cpu',
        'disk',
        'use_double_quant',
        'bf16',
        'trust_remote_code',
        'no_use_fast',
    ],
    'ExLlamav3_HF': [
        'ctx_size',
        'cache_type',
        'gpu_split',
        'cfg_cache',
        'trust_remote_code',
        'no_use_fast',
    ],
    'ExLlamav2_HF': [
        'ctx_size',
        'cache_type',
        'gpu_split',
        'alpha_value',
        'compress_pos_emb',
        'num_experts_per_token',
        'autosplit',
        'enable_tp',
        'no_flash_attn',
        'no_xformers',
        'no_sdpa',
        'cfg_cache',
        'trust_remote_code',
        'no_use_fast',
    ],
    'ExLlamav2': [
        'ctx_size',
        'cache_type',
        'gpu_split',
        'alpha_value',
        'compress_pos_emb',
        'num_experts_per_token',
        'autosplit',
        'enable_tp',
        'no_flash_attn',
        'no_xformers',
        'no_sdpa',
        'model_draft',
        'draft_max',
        'ctx_size_draft',
        'speculative_decoding_accordion',
    ],
    'TensorRT-LLM': [
        'ctx_size',
        'cpp_runner',
        'tensorrt_llm_info',
    ]
})


def transformers_samplers():
    return {
        'temperature',
        'dynatemp_low',
        'dynatemp_high',
        'dynatemp_exponent',
        'smoothing_factor',
        'smoothing_curve',
        'min_p',
        'top_p',
        'top_k',
        'typical_p',
        'xtc_threshold',
        'xtc_probability',
        'epsilon_cutoff',
        'eta_cutoff',
        'tfs',
        'top_a',
        'top_n_sigma',
        'dry_multiplier',
        'dry_allowed_length',
        'dry_base',
        'repetition_penalty',
        'frequency_penalty',
        'presence_penalty',
        'encoder_repetition_penalty',
        'no_repeat_ngram_size',
        'repetition_penalty_range',
        'penalty_alpha',
        'guidance_scale',
        'mirostat_mode',
        'mirostat_tau',
        'mirostat_eta',
        'prompt_lookup_num_tokens',
        'do_sample',
        'dynamic_temperature',
        'temperature_last',
        'auto_max_new_tokens',
        'ban_eos_token',
        'add_bos_token',
        'enable_thinking',
        'skip_special_tokens',
        'static_cache',
        'seed',
        'sampler_priority',
        'custom_token_bans',
        'negative_prompt',
        'dry_sequence_breakers',
        'grammar_string',
        'grammar_file_row',
    }


loaders_samplers = {
    'Transformers': transformers_samplers(),
    'ExLlamav3_HF': {
        'temperature',
        'dynatemp_low',
        'dynatemp_high',
        'dynatemp_exponent',
        'smoothing_factor',
        'smoothing_curve',
        'min_p',
        'top_p',
        'top_k',
        'typical_p',
        'xtc_threshold',
        'xtc_probability',
        'epsilon_cutoff',
        'eta_cutoff',
        'tfs',
        'top_a',
        'top_n_sigma',
        'dry_multiplier',
        'dry_allowed_length',
        'dry_base',
        'repetition_penalty',
        'frequency_penalty',
        'presence_penalty',
        'encoder_repetition_penalty',
        'no_repeat_ngram_size',
        'repetition_penalty_range',
        'guidance_scale',
        'mirostat_mode',
        'mirostat_tau',
        'mirostat_eta',
        'do_sample',
        'dynamic_temperature',
        'temperature_last',
        'auto_max_new_tokens',
        'ban_eos_token',
        'add_bos_token',
        'enable_thinking',
        'skip_special_tokens',
        'seed',
        'sampler_priority',
        'custom_token_bans',
        'negative_prompt',
        'dry_sequence_breakers',
        'grammar_string',
        'grammar_file_row',
    },
    'ExLlamav2_HF': {
        'temperature',
        'dynatemp_low',
        'dynatemp_high',
        'dynatemp_exponent',
        'smoothing_factor',
        'smoothing_curve',
        'min_p',
        'top_p',
        'top_k',
        'typical_p',
        'xtc_threshold',
        'xtc_probability',
        'epsilon_cutoff',
        'eta_cutoff',
        'tfs',
        'top_a',
        'top_n_sigma',
        'dry_multiplier',
        'dry_allowed_length',
        'dry_base',
        'repetition_penalty',
        'frequency_penalty',
        'presence_penalty',
        'encoder_repetition_penalty',
        'no_repeat_ngram_size',
        'repetition_penalty_range',
        'guidance_scale',
        'mirostat_mode',
        'mirostat_tau',
        'mirostat_eta',
        'do_sample',
        'dynamic_temperature',
        'temperature_last',
        'auto_max_new_tokens',
        'ban_eos_token',
        'add_bos_token',
        'enable_thinking',
        'skip_special_tokens',
        'seed',
        'sampler_priority',
        'custom_token_bans',
        'negative_prompt',
        'dry_sequence_breakers',
        'grammar_string',
        'grammar_file_row',
    },
    'ExLlamav2': {
        'temperature',
        'dynatemp_low',
        'dynatemp_high',
        'dynatemp_exponent',
        'smoothing_factor',
        'min_p',
        'top_p',
        'top_k',
        'typical_p',
        'xtc_threshold',
        'xtc_probability',
        'tfs',
        'top_a',
        'dry_multiplier',
        'dry_allowed_length',
        'dry_base',
        'repetition_penalty',
        'frequency_penalty',
        'presence_penalty',
        'repetition_penalty_range',
        'mirostat_mode',
        'mirostat_tau',
        'mirostat_eta',
        'dynamic_temperature',
        'temperature_last',
        'auto_max_new_tokens',
        'ban_eos_token',
        'add_bos_token',
        'enable_thinking',
        'skip_special_tokens',
        'seed',
        'custom_token_bans',
        'dry_sequence_breakers',
    },
    'llama.cpp': {
        'temperature',
        'dynatemp_low',
        'dynatemp_high',
        'dynatemp_exponent',
        'min_p',
        'top_p',
        'top_k',
        'typical_p',
        'xtc_threshold',
        'xtc_probability',
        'top_n_sigma',
        'dry_multiplier',
        'dry_allowed_length',
        'dry_base',
        'repetition_penalty',
        'frequency_penalty',
        'presence_penalty',
        'repetition_penalty_range',
        'mirostat_mode',
        'mirostat_tau',
        'mirostat_eta',
        'dynamic_temperature',
        'temperature_last',
        'auto_max_new_tokens',
        'ban_eos_token',
        'add_bos_token',
        'enable_thinking',
        'seed',
        'sampler_priority',
        'dry_sequence_breakers',
        'grammar_string',
        'grammar_file_row',
    },
    'TensorRT-LLM': {
        'temperature',
        'top_p',
        'top_k',
        'repetition_penalty',
        'frequency_penalty',
        'presence_penalty',
        'auto_max_new_tokens',
        'ban_eos_token',
    }
}


@functools.cache
def list_all_samplers():
    all_samplers = set()
    for k in loaders_samplers:
        for sampler in loaders_samplers[k]:
            all_samplers.add(sampler)

    return sorted(all_samplers)


def blacklist_samplers(loader, dynamic_temperature):
    all_samplers = list_all_samplers()
    output = []

    for sampler in all_samplers:
        if loader == 'All' or sampler in loaders_samplers[loader]:
            if sampler.startswith('dynatemp'):
                output.append(gr.update(visible=dynamic_temperature))
            else:
                output.append(gr.update(visible=True))
        else:
            output.append(gr.update(visible=False))

    return output


@functools.cache
def get_all_params():
    all_params = set()
    for k in loaders_and_params:
        for el in loaders_and_params[k]:
            all_params.add(el)

    return sorted(all_params)


def make_loader_params_visible(loader):
    params = []
    all_params = get_all_params()
    if loader in loaders_and_params:
        params = loaders_and_params[loader]

    return [gr.update(visible=True) if k in params else gr.update(visible=False) for k in all_params]
