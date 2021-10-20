1. What are `orchestrators` ?
   - Apache Airflow, Apache Beam and Kubeflow pipelines are orchestrators
2. What are `artifcats` ?
   - Artifacts are the outputs of steps in a TFX pipeline. Subsequent steps may use those artifacts. This way TFX lets you transfer data between workflow steps.
   - For example `ExampleGEn` standard component emits serialized examples, which are used as inputs by components such as `StatisticsGen`
3. What are the `Components` ?
   - An ml task that you apply in a step.
   - Composed of: 
     - Component specification: defines its input and output artifacts
     - Executor: which implements the code to perform a step
     - Component interface: packages the component specification and executor for use in a pipeline
4. 

