# Script de correction automatique CI - tabular-benchmark-mlops
# Auteur : valorisa

$ErrorActionPreference = "Stop"
Set-Location $PSScriptRoot\..

Write-Host "============================================================" -ForegroundColor Cyan
Write-Host "  Correction Automatique CI" -ForegroundColor Cyan
Write-Host "============================================================" -ForegroundColor Cyan

Write-Host "`n[1/5] Activation environnement virtuel..." -ForegroundColor Yellow
& .\.venv\Scripts\Activate.ps1
Write-Host "  ✓ Activé" -ForegroundColor Green

Write-Host "`n[2/5] Vérification outils..." -ForegroundColor Yellow
foreach ($tool in @("black", "isort", "flake8")) {
    if (-not (Get-Command $tool -ErrorAction SilentlyContinue)) {
        Write-Host "  Installation de $tool..." -ForegroundColor Yellow
        pip install $tool --quiet
    }
}
Write-Host "  ✓ Outils prêts" -ForegroundColor Green

Write-Host "`n[3/5] Sauvegarde..." -ForegroundColor Yellow
$backupDir = "backup-$(Get-Date -Format 'yyyyMMdd-HHmmss')"
New-Item -ItemType Directory -Force -Path $backupDir | Out-Null
Copy-Item -Path "src\*.py" -Destination $backupDir\src\ -Force -ErrorAction SilentlyContinue
Copy-Item -Path "tests\*.py" -Destination $backupDir\tests\ -Force -ErrorAction SilentlyContinue
Write-Host "  ✓ Sauvegarde : $backupDir" -ForegroundColor Green

Write-Host "`n[4/5] Correction Black + isort..." -ForegroundColor Yellow
black src/ tests/ --line-length 88
isort src/ tests/ --profile black
Write-Host "  ✓ Formatage appliqué" -ForegroundColor Green

Write-Host "`n[5/5] Vérification flake8..." -ForegroundColor Yellow
flake8 src/ tests/ --max-line-length=88 --ignore=E203,W503
if ($LASTEXITCODE -eq 0) {
    Write-Host "  ✓ flake8 : OK" -ForegroundColor Green
} else {
    Write-Host "  ⚠ Corrections manuelles nécessaires" -ForegroundColor Yellow
}

Write-Host "`n============================================================" -ForegroundColor Cyan
Write-Host "  ✅ Terminé !" -ForegroundColor Green
Write-Host "============================================================" -ForegroundColor Cyan
Write-Host "`nExécutez :" -ForegroundColor Yellow
Write-Host "  git add ." -ForegroundColor Cyan
Write-Host "  git commit -m 'fix: pre-commit auto-fixes'" -ForegroundColor Cyan
Write-Host "  git push origin main" -ForegroundColor Cyan
Write-Host "============================================================`n" -ForegroundColor Cyan
