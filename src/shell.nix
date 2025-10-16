{ pkgs ? import <nixpkgs> {} }:

pkgs.mkShell {
  name = "concord-env";

  buildInputs = with pkgs; [
    gcc
    cmake
    git
    pkg-config
    concord
    jansson
    libwebsockets
    curl
  ];
}
