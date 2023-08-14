{
    inputs = {
        nixpkgs.url = "nixpkgs/nixos-23.05";
    };

    outputs = { self, nixpkgs, ...}@inputs:
    let
      forAllSystems = nixpkgs.lib.genAttrs supportedSystems;
      pkgs = nixpkgs.legacyPackages.${system};
    in
    {
      packages = forAllSystems (system:
        {
            devShells.${system}.default = import ./shell.nix { inherit pkgs; };
        });

    }
}
