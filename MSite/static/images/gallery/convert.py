#!/usr/bin/env python3
"""
HEIC to JPG Converter for Gallery Images

This script converts HEIC images to JPG format for better web browser compatibility.
It will scan a directory for HEIC files and create JPG versions while preserving the originals.

Requirements:
    pip install pillow-heif Pillow

Usage:
    python heic_to_jpg_converter.py
"""

import os
import sys
from pathlib import Path
import logging

try:
    from PIL import Image
    import pillow_heif
except ImportError:
    print("Required libraries not found. Please install them with:")
    print("pip install pillow-heif Pillow")
    sys.exit(1)

# Register HEIF/HEIC file format with Pillow
pillow_heif.register_heif_opener()

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

def convert_heic_to_jpg(heic_path, quality=95):
    """
    Convert a HEIC file to JPG format
    
    Args:
        heic_path (Path): Path to the HEIC file
        quality (int): JPG quality (1-100, higher is better)
        
    Returns:
        Path: Path to the converted JPG file
    """
    try:
        # Open the HEIC file
        with Image.open(heic_path) as img:
            # Create output path with JPG extension
            jpg_path = heic_path.with_suffix('.jpg')
            
            # Convert to RGB mode if necessary (in case of RGBA images)
            if img.mode != 'RGB':
                img = img.convert('RGB')
                
            # Save as JPG
            img.save(jpg_path, 'JPEG', quality=quality)
            
            logging.info(f"Converted: {heic_path.name} → {jpg_path.name}")
            return jpg_path
            
    except Exception as e:
        logging.error(f"Failed to convert {heic_path}: {str(e)}")
        return None

def scan_and_convert_directory(directory_path, quality=95):
    """
    Scan a directory for HEIC files and convert them to JPG
    
    Args:
        directory_path (str): Path to the directory to scan
        quality (int): JPG quality (1-100, higher is better)
        
    Returns:
        int: Number of successfully converted files
    """
    directory = Path(directory_path)
    if not directory.exists() or not directory.is_dir():
        logging.error(f"Directory not found: {directory_path}")
        return 0
        
    # Find all HEIC files (case insensitive)
    heic_files = list(directory.glob('**/*.heic')) + list(directory.glob('**/*.HEIC'))
    
    if not heic_files:
        logging.info(f"No HEIC files found in {directory_path}")
        return 0
        
    logging.info(f"Found {len(heic_files)} HEIC files in {directory_path}")
    
    # Convert each file
    success_count = 0
    for heic_file in heic_files:
        jpg_path = convert_heic_to_jpg(heic_file, quality)
        if jpg_path:
            success_count += 1
    
    logging.info(f"Conversion complete. Successfully converted {success_count}/{len(heic_files)} files.")
    return success_count

def main():
    """Main function to run the converter"""
    
    # Default gallery directory based on Flask app structure
    default_gallery_dir = Path("static/images/gallery")
    
    # Allow user to specify a different directory
    if len(sys.argv) > 1:
        gallery_dir = sys.argv[1]
    else:
        # Check if we're in the Flask app root or in a subdirectory
        if (Path.cwd() / default_gallery_dir).exists():
            gallery_dir = str(default_gallery_dir)
        elif (Path.cwd().parent / default_gallery_dir).exists():
            gallery_dir = str(Path.cwd().parent / default_gallery_dir)
        else:
            gallery_dir = input("Enter the path to your gallery directory: ")
    
    logging.info(f"Starting HEIC to JPG conversion in: {gallery_dir}")
    
    # Convert with high quality (95)
    scan_and_convert_directory(gallery_dir, quality=95)
    
    logging.info("Done! Your gallery should now have JPG versions of all HEIC files.")
    logging.info("Make sure to update your gallery.html to use the .jpg extensions instead of .heic")

if __name__ == "__main__":
    main()