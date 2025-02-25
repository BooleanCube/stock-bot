{ pkgs ? import <nixpkgs> {} }:

pkgs.mkShell {
  buildInputs = with pkgs; [
    (python312.withPackages (ps: with ps; [
      tkinter
      pip
      numpy
      pandas
      matplotlib
      peewee
      scipy
      python-dateutil
      yfinance
    ]))
  ];

  shellHook = ''
    # Print environment info
    echo "Python environment activated with tkinter support"
    python -c "import sys; print(f'Python version: {sys.version}')"
  '';
}