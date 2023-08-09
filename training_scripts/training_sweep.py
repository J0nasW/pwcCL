# Write a python script that calls the paperswithcode_cl_trainer_auto.py script with a range of arguments

import os

# Set the name of the model to be saved
CUSTOM_MODEL_NAME = "pwcCL_sweep/pwcCL"
TRAINING_CSV = "../papers.csv"
SAMPLE_SIZE = None
ALLOW_DUPLICATE_CLASSES = [False]
FORCE_BALANCED_DATASET = [False]
NUM_EPOCHS = [20]
BATCH_SIZE = [16]
COLUMN_NAME = ["areaID", "taskID"]

print("Starting training sweep")
print("")

# Call the paperswithcode_cl_trainer_auto.py script with a range of arguments
for allow_duplicate_classes in ALLOW_DUPLICATE_CLASSES:
    for force_balanced_dataset in FORCE_BALANCED_DATASET:
        for num_epochs in NUM_EPOCHS:
            for batch_size in BATCH_SIZE:
                for column_name in COLUMN_NAME:
                    try:
                        print("Starting new training run...")
                        os_command = f"python paperswithcode_cl_trainer_auto.py -n {CUSTOM_MODEL_NAME} -c {TRAINING_CSV} {'-s {SAMPLE_SIZE} ' if SAMPLE_SIZE else ''}-e {num_epochs} -b {batch_size} -col {column_name} {'-d ' if allow_duplicate_classes else ''}{'-fb ' if force_balanced_dataset else ''}"
                        print(f"Running command: {os_command}")
                        print("")
                        os.system(os_command)
                    except:
                        print("Error in training with arguments: -n " + CUSTOM_MODEL_NAME + " -c " + TRAINING_CSV + " -e " + str(num_epochs) + " -b " + str(batch_size) + " -col " + column_name + " -d " + str(allow_duplicate_classes) + " -fb " + str(force_balanced_dataset))
                        continue

print("")
print("Finished training sweep")
