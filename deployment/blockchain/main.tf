data "random_id" "random_trail" {}

resource "google_compute_network" "vpc_network" {
  name                    = "voting-network-${data.random_id.random_trail.id}"
  auto_create_subnetworks = false
  mtu                     = 1460
}

resource "google_compute_subnetwork" "default" {
  name          = "voting-subnet-for-${google_compute_network.vpc_network.name}"
  ip_cidr_range = "10.0.1.0/24"
  region        = "us-west1"
  network       = google_compute_network.vpc_network.id
}