terraform {
  required_providers {
    docker = {
      source  = "kreuzwerker/docker"
      version = "~> 2.23.0"
    }
  }
}



provider "docker" {}

resource "docker_image" "ml_model_image" {
  name = "ml-model"
  build {
    path = "../src/"  # Path to ML model Dockerfile
  }
}

resource "docker_container" "ml_model_container" {
  image = docker_image.ml_model_image.latest
  name  = "ml-model-container"
  ports {
    internal = 5000
    external = 5000
  }
}
