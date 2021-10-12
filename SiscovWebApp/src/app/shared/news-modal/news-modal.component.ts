import { Component, EventEmitter, Input, OnInit, Output } from '@angular/core';

@Component({
  selector: 'app-news-modal',
  templateUrl: './news-modal.component.html',
  styleUrls: ['./news-modal.component.css']
})
export class NewsModalComponent implements OnInit {

  @Input() localName: string;
  @Input() isOpen: boolean = false;
  @Output() close = new EventEmitter();
  img = '../../assets/bandeira-acre.png'
  news = [{title: "Variante Delta encontrada em Acrelândia", link: 'https://google.com', id: 1}, 
          {title: "Variante Omega encontrada em Acrelândia", link: 'https://google.com', id: 2}, 
          {title: "Variante Zeta encontrada em Acrelândia", link: 'https://google.com', id: 3}, 
          {title: "Variante Pica-Pau encontrada em Acrelândia", link: 'https://google.com', id: 4}, 
          {title: "Variante Gohan encontrada em Acrelândia", link: 'https://google.com', id: 5},
        ] 


  constructor() { }

  ngOnInit(): void {
  }

  closeNewsModal() {
    this.close.emit();
  }

}
