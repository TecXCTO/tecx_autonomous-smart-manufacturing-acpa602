#!/usr/bin/env python3
# Post-Training Quantization Calibration Framework
import os
import sys
import numpy as np
import tensorflow as tf

def calibration_data_feed_generator():
    """Generates standard tensor maps to calibrate integer scaling limits."""
    # In production, read raw image matrices directly from datasets/calibration_meltpool/
    for _ in range(100):
        dummy_pixel_array = np.random.rand(1, 64, 64, 1).astype(np.float32)
        yield [dummy_pixel_array]

def compile_and_quantize_network(source_dir, output_file_path):
    if not os.path.exists(source_dir):
        print(f"Error: Target source directory {source_dir} unresolvable.")
        sys.exit(1)
        
    converter = tf.lite.TFLiteConverter.from_saved_model(source_dir)
    converter.optimizations = [tf.lite.Optimize.DEFAULT]
    converter.representative_dataset = calibration_data_feed_generator
    
    # Enforce strict 8-bit integer operations to unlock NPU acceleration
    converter.target_spec.supported_ops = [tf.lite.OpsSet.TFLITE_BUILTINS_INT8]
    converter.inference_input_type = tf.int8
    converter.inference_output_type = tf.int8
    
    print("Beginning Post-Training Quantization cycle...")
    quantized_binary = converter.convert()
    
    with open(output_file_path, "wb") as f:
        f.write(quantized_binary)
    print(f"Success: Optimized NPU model file written to -> {output_file_path}")

if __name__ == "__main__":
    compile_and_quantize_network("models/saved_model_fp32", "models/int8_meltpool_net.tflite")
  
