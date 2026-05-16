import os
from pathlib import Path
from typing import List

def get_java_files(project_path: str) -> List[str]:
    """Récupère tous les fichiers Java du projet"""
    java_files = []
    for root, dirs, files in os.walk(project_path):
        dirs[:] = [
            d for d in dirs
            if d not in ['target', '.git', '.idea', 'node_modules']
        ]
        for file in files:
            if file.endswith('.java'):
                java_files.append(os.path.join(root, file))
    return java_files

def get_feature_files(project_path: str) -> List[str]:
    """Récupère tous les fichiers .feature du projet"""
    feature_files = []
    for root, dirs, files in os.walk(project_path):
        dirs[:] = [
            d for d in dirs
            if d not in ['target', '.git']
        ]
        for file in files:
            if file.endswith('.feature'):
                feature_files.append(os.path.join(root, file))
    return feature_files

def read_file(file_path: str) -> str:
    """Lit le contenu d'un fichier"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return f.read()
    except UnicodeDecodeError:
        with open(file_path, 'r', encoding='latin-1') as f:
            return f.read()

def get_file_name(file_path: str) -> str:
    """Retourne le nom du fichier sans le chemin"""
    return Path(file_path).name
