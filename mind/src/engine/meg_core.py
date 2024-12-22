import json
import os
from typing import Dict, List, Generator
from time import sleep
import sys

class MEGCore:
    def __init__(self, memories_path: str = "memories/"):
        self.memories_path = memories_path
        self.current_memory = None

    def show_loading_bar(self, duration: float = 3.0, width: int = 40) -> None:
        """Mostra una barra di caricamento della memoria"""
        print("\nCaricamento memoria in corso...")
        for i in range(width + 1):
            progress = i / width
            bar = "█" * i + "░" * (width - i)
            percentage = int(progress * 100)
            sys.stdout.write(f"\r[{bar}] {percentage}%")
            sys.stdout.flush()
            sleep(duration / width)
        print("\n")

    def memory_initialization(self) -> None:
        """Sequenza di inizializzazione memoria"""
        print("\nInizializzazione M.E.G. System...")
        sleep(0.5)
        print("Connessione al database memorie...")
        sleep(0.5)
        print("Calibrazione parametri neurali...")
        sleep(0.5)
        self.show_loading_bar()
        print("Sistema pronto per la riproduzione.\n")

    def load_memory(self, memory_path: str) -> Dict:
        """Carica un singolo ricordo dal file json"""
        with open(memory_path, 'r', encoding='utf-8') as f:
            return json.load(f)

    def play_memory(self, memory_data: Dict, speed: float = 1.0) -> None:
        """Riproduce un ricordo in modo immersivo"""
        self.memory_initialization()
        
        print("\n=== INIZIO MEMORIA ===")
        print(f"Esploratore: {memory_data['explorer']['name']}")
        print(f"Data: {memory_data['memory']['date']}")
        print(f"Luogo: {memory_data['memory']['location']}")
        print("\nRicordo in riproduzione...")
        sleep(2)  # Pausa drammatica

        # Divide il contenuto in paragrafi e li riproduce con pause
        paragraphs = memory_data['memory']['content'].split('\n')
        for paragraph in paragraphs:
            if paragraph.strip():
                print(f"\n{paragraph.strip()}")
                sleep(len(paragraph) * 0.05 / speed)  # Pausa proporzionale alla lunghezza

        print("\n=== FINE MEMORIA ===")

    def play_all_memories(self, speed: float = 1.0) -> None:
        """Riproduce tutti i ricordi in sequenza"""
        print("M.E.G. System - Memory Explorer Gateway")
        print("======================================")
        
        for explorer_dir in os.listdir(self.memories_path):
            explorer_path = os.path.join(self.memories_path, explorer_dir)
            if os.path.isdir(explorer_path):
                for memory_file in os.listdir(explorer_path):
                    if memory_file.endswith('.json'):
                        memory_path = os.path.join(explorer_path, memory_file)
                        memory_data = self.load_memory(memory_path)
                        self.play_memory(memory_data, speed)
                        input("\nPremi INVIO per il prossimo ricordo...")
                        print("\nDisconnessione memoria in corso...")
                        self.show_loading_bar(1.0)  # Barra di scaricamento più veloce

def main():
    meg = MEGCore()
    meg.play_all_memories(speed=1.0)

if __name__ == "__main__":
    main()