1. To run a tensorflow model in gcloud ai platform locally. This will run in a similar environment to the cloud but will run in your local machine.

   ```bash
   gcloud ai-platform local train --module-name trainer.iris --package-path trainer --job-dir export
   ```

   -> module name : name of the script that runs the training

   -> package-path: path to the folder that converted to a package. Module-name meaning training script also resides here

   -> job-dir: is the input parameter needed by the code, it may not be needed in your code

2. 