import { Component, EventEmitter, Input, OnInit, Output } from '@angular/core';
import { NewsService } from './services/news.service';
import { map } from 'rxjs/operators'

@Component({
  selector: 'app-news-modal',
  templateUrl: './news-modal.component.html',
  styleUrls: ['./news-modal.component.css']
})
export class NewsModalComponent implements OnInit {

  @Input() localName: string = "Acrelândia";
  @Input() isOpen: boolean = false;
  @Input() variantLocal;
  @Input() variantStateId?;
  @Output() close = new EventEmitter();
  img = '../../assets/bandeira-acre.png'
  loading: boolean = false;
  news;


  constructor(private newsService: NewsService) { }

  ngOnInit(): void {
    this.loading = true;
    this.newsService.listAllCountyNews(this.variantStateId, this.variantLocal.id)
    .pipe(
      map(data => {
        //return data.forEach(item => item.split(': ')[1]);
      })
    ).subscribe(news => {
      this.news = news;
      console.log("news: ", news);
      this.loading = false;
    })
    // setTimeout(() => {
    //   this.news = [{title: "Variante Delta encontrada em Acrelândia após examinar paciente vindo do exterior", link: 'https://google.com', id: 1}, 
    //               {title: "Variante Omega encontrada em Acrelândia após examinar paciente vindo do exterior", link: 'https://google.com', id: 2}, 
    //               {title: "Variante Zeta encontrada em Acrelândia após examinar paciente vindo do exterior", link: 'https://google.com', id: 3}, 
    //               {title: "Variante Pica-Pau encontrada em Acrelândia após examinar paciente vindo do exterior", link: 'https://google.com', id: 4}, 
    //               {title: "Variante Gohan encontrada em Acrelândia após examinar paciente vindo do exterior", link: 'https://google.com', id: 5},
    //               ] 
    //   this.loading = false;
    //   console.log("Id do local a se fazer a query: ", this.variantLocal);
    // }, 3000);
  }

  closeNewsModal() {
    this.close.emit();
  }

}
