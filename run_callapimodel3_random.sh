#!/bin/bash

# Array of image file names
images=("adeno.jpg" "large.jpg" "normal.jpg" "squamous.jpg")

# Outer loop to run the process 100 times
for i in {1..100}; do
    echo "Iteration: $i"

    # Randomly shuffle the array
    shuffled_images=($(shuf -e "${images[@]}"))

    # Run the Python script with the shuffled images
    echo "Running callapimodel3.py with order: ${shuffled_images[0]}, ${shuffled_images[1]}, ${shuffled_images[2]}, ${shuffled_images[3]}"
    python callapimodel3.py "${shuffled_images[0]}" "${shuffled_images[1]}" "${shuffled_images[2]}" "${shuffled_images[3]}"
done

