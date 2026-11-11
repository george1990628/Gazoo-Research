# USC Keck: clinical data analysis

During my research at USC Keck, I used Pandas to organize clinical records, plot PSA measurements and disease-stage data, and calculate the time between surgery and biochemical progression. I also tried nearest-neighbor matching and image similarity with a pretrained ViT.

The examples in this repo use **synthetic data**. No patient records or saved clinical-data outputs are included.

## Files

| File | What it does |
| --- | --- |
| [George.ipynb](George.ipynb) | Filters and reshapes records, plots the data, and demonstrates nearest-neighbor lookup. |
| [ViT image similarity](notebooks/vit_image_similarity.ipynb) | Compares cat, dog, and query images using ViT embeddings and cosine similarity. |
| [DOCX-to-PDF utility](tools/docx_to_pdf.py) | Converts paragraph text from a Word file to PDF. |

## Run the analysis

```bash
python -m pip install -r requirements.txt
```

Open `George.ipynb` in Jupyter or Colab and run the cells in order. It creates the synthetic records inside the notebook, so there is no data file to upload.

The image and document examples need the packages in `requirements-optional.txt` and your own sample files.

## Notes

The synthetic data is there to show how the code works. Its plots do not establish clinical relationships. The date calculation does not account for censoring, and the nearest-neighbor example is a simple lookup using two variables. The ViT example uses ordinary images.

The document converter handles paragraph text only. It does not preserve complex Word formatting and replaces characters outside Latin-1.

I cleaned up the original notebook by fixing the `Print` typo, aligning the filter mask with the DataFrame index, converting model inputs to numbers, and removing chained assignment. The ViT example now uses evaluation mode and RGB images. The Pandas notebook was checked using the synthetic data.
