#!/bin/bash
echo "BlockOS ISO építése..."
mkdir -p build_iso
cp -r apps build_iso/
cp -r system build_iso/
cp -r installer build_iso/
cp bootloader/grub.cfg build_iso/
# genisoimage -o BlockOS.iso ./build_iso
echo "Kész! A BlockOS.iso Rufus-szal írható."