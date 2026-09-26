# Disease Detection API Contract (v1)

## Endpoint
POST /predict

## Request
Content-Type: multipart/form-data
Field: `image` (JPG or PNG leaf photo)

## Success Response (200)
{
  "disease": "RedRot sugarcane",
  "confidence": 0.9988,
  "low_confidence": false
}

## Error Responses
- 400 {"error": "no image provided"}
- 500 {"error": "prediction failed"}

## Supported classes (v1)
1. Healthy Maize
2. Mosaic sugarcane
3. RedRot sugarcane
4. RedRust sugarcane
5. Sugarcane Healthy
6. Yellow Rust Sugarcane
7. maize ear rot
8. maize fall armyworm
9. maize stem borer

## Known limitations
- Yellow Rust Sugarcane unreliable (only 4 validation images)
- Mosaic ↔ Sugarcane Healthy ~15% confusion