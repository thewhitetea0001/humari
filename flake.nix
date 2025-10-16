{
  description = "Dev shell with concord";

  inputs.nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";

  outputs = { self, nixpkgs }: {
    devShells.x86_64-linux.default = let
      pkgs = import nixpkgs { system = "x86_64-linux"; };
    in pkgs.mkShell {
      name = "concord-env";
      buildInputs = with pkgs; [ concord gcc cmake git ];
    };
  };
}
