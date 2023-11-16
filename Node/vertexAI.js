const {ModelServiceClient} = require('@google-cloud/aiplatform');
const aiplatform = require('@google-cloud/aiplatform');
const {PipelineServiceClient} = aiplatform.v1;


const clientOptions = {
  apiEndpoint: 'us-central1-aiplatform.googleapis.com',
};

const modelServiceClient = new ModelServiceClient(clientOptions);
const pipelineClient = new PipelineServiceClient(clientOptions);