{
    inputs = {
        nixpkgs.url = "nixpkgs/nixos-23.05";
    };

    outputs = { self, nixpkgs, ...}@inputs:
    let
      pkgs = nixpkgs.legacyPackages.x86_64-linux;
    in
    {
        devShells.x86_64-linux.default = import ./shell.nix { inherit pkgs; };

    };
}
