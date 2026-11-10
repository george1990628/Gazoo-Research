# USC Keck research: exploratory record analysis

**Status: historical research code (2024); public example uses synthetic data.**

Exploratory analysis from my USC Keck radiation-oncology research experience. The uploaded notebook implements tagged-record filtering and reshaping, event-date calculations, stage and PSA plots, standardized nearest-neighbor lookup, and a separate ViT image-similarity toy example.

## Included work

| File | Purpose |
| --- | --- |
| [George.ipynb](George.ipynb) | Self-contained analysis using invented demonstration records. |
| [ViT image similarity](notebooks/vit_image_similarity.ipynb) | Compare cat/dog/query images using a pretrained ViT embedding and cosine similarity. |
| [DOCX utility](tools/docx_to_pdf.py) | Original paragraph-only document converter, separated from the analysis. |

## Run the analysis

Install the core packages, open `George.ipynb` in Jupyter or Colab, and run the cells in order:

```bash
python -m pip install -r requirements.txt
```

No clinical file upload is required. The synthetic records are created inside the notebook. The optional image and document utilities require `requirements-optional.txt` and user-supplied example files.

## Scope and interpretation

The public notebook contains no source patient records or saved clinical-data outputs. The synthetic values illustrate software behavior only. The event-interval calculation is not survival analysis; the nearest-neighbor example is not a validated clinical model. ViT is demonstrated on ordinary images, not a reproduced clinical image-retrieval evaluation.

The document utility converts paragraph text only and substitutes characters outside Latin-1; it does not preserve complex Word layouts.

## Public preparation

Saved outputs, widget metadata, source record references, and personal Drive paths were removed. The analysis now creates synthetic input, fixes the original `Print` typo and Pandas mask-index alignment, converts nearest-neighbor inputs to numeric values, and avoids chained assignment. The ViT example explicitly uses evaluation mode and RGB images. These are disclosed maintenance changes; no experiment results were invented.

The Pandas analysis ran locally against the synthetic data. Optional pretrained-model inference and PDF conversion were not rerun during portfolio preparation. Third-party packages and model weights retain their original terms.
