"""
config.py
Configuration settings (parameters) for data processing.
"""

config_sim = {
    'fs': 1000,
    'lowpass_fc': 40,
    'lowpass_n_seconds': .1,
    'freq_osc': 10,
    'f_range': (6, 14),
    'f_range_noise': (1, None),
    'filter_order_noise': 3001,
    'cycle_features': {'amp_std': .2,
                       'period_std': 15,
                       'rdsym_std': .1},
    'cycle_features_2': {'amp_std': .1,
                       'period_std': 5,
                       'rdsym_std': .05},
    'osc_detect_kwargs': {'amplitude_fraction_threshold':0,
                          'amplitude_consistency_threshold':.5,
                          'period_consistency_threshold':.5,
                          'monotonicity_threshold':.8,
                          'N_cycles_min':3},
    'osc_detect_kwargs_conservative': {'amplitude_fraction_threshold':0,
                          'amplitude_consistency_threshold':.6,
                          'period_consistency_threshold':.6,
                          'monotonicity_threshold':.9,
                          'N_cycles_min':3}

}