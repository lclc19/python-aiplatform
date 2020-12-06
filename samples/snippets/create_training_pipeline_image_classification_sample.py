# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# [START aiplatform_create_training_pipeline_image_classification_sample]
from google.cloud import aiplatform
from google.cloud.aiplatform_v1beta1.services import pipeline_service
from google.protobuf import json_format

# Import the enhanced types
from google.cloud.aiplatform.v1beta1.schema.trainingjob import definition
ModelType = definition.AutoMlImageClassificationInputs().ModelType


def create_training_pipeline_image_classification_sample(
    display_name: str, dataset_id: str, model_display_name: str, project: str
):
    client_options = dict(api_endpoint="us-central1-aiplatform.googleapis.com")
    client = pipeline_service.PipelineServiceClient(client_options=client_options)
    location = "us-central1"
    parent = "projects/{project}/locations/{location}".format(
        project=project, location=location
    )

    icn_training_inputs = definition.AutoMlImageClassificationInputs(
        multi_label=True,
        model_type=ModelType.CLOUD,
        budget_milli_node_hours=8000,
        disable_early_stopping=False
    )

    training_pipeline = {
        "display_name": display_name,
        "training_task_definition": "gs://google-cloud-aiplatform/schema/trainingjob/definition/automl_image_classification_1.0.0.yaml",
        "training_task_inputs": icn_training_inputs.to_value(),
        "input_data_config": {"dataset_id": dataset_id},
        "model_to_upload": {"display_name": model_display_name},
    }

    response = client.create_training_pipeline(
        parent=parent, training_pipeline=training_pipeline
    )
    print("response:", response)
# [END aiplatform_create_training_pipeline_image_classification_sample]