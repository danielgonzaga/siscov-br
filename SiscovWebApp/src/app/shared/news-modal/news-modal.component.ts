import { Component, EventEmitter, Input, OnInit, Output } from '@angular/core';

@Component({
  selector: 'app-news-modal',
  templateUrl: './news-modal.component.html',
  styleUrls: ['./news-modal.component.css']
})
export class NewsModalComponent implements OnInit {

  @Input() localName: string = "Acrelândia";
  @Input() isOpen: boolean = false;
  @Output() close = new EventEmitter();
  img = '../../assets/bandeira-acre.png'
  loading: boolean = false;
  news;


  constructor() { }

  ngOnInit(): void {
    this.loading = true;
    setTimeout(() => {
      this.news = [{title: "Variante Delta encontrada em Acrelândia após examinar paciente vindo do exterior", link: 'https://google.com', id: 1}, 
                  {title: "Variante Omega encontrada em Acrelândia após examinar paciente vindo do exterior", link: 'https://google.com', id: 2}, 
                  {title: "Variante Zeta encontrada em Acrelândia após examinar paciente vindo do exterior", link: 'https://google.com', id: 3}, 
                  {title: "Variante Pica-Pau encontrada em Acrelândia após examinar paciente vindo do exterior", link: 'https://google.com', id: 4}, 
                  {title: "Variante Gohan encontrada em Acrelândia após examinar paciente vindo do exterior", link: 'https://google.com', id: 5},
                  ] 
      this.loading = false;
    }, 3000);
  }

  closeNewsModal() {
    this.close.emit();
  }

}
