{
  "targets": [
    {
      "include_dirs": [
        "<!(node -e \"require('nan')\")"
      ],
      "target_name": "addon",
      "sources": [ "src/main.cpp" ],
      "cflags!": ["-fno-exceptions"],
      "cflags_cc!": ["-fno-exceptions"],
      "defines!": ["_HAS_EXCEPTIONS=0"],
      "msvs_settings": {
        "VCCLCompilerTool": { "ExceptionHandling": 1 },  # /EHsc
      }
    }
  ]
}
