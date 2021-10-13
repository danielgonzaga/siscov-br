import { Component, EventEmitter, Input, OnInit, Output } from '@angular/core';
import { NewsService } from './services/news.service';
import { takeUntil } from 'rxjs/operators'
import { Subject } from 'rxjs';

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
  loading: boolean = false;
  news;
  private destroy$ = new Subject<boolean>();

  constructor(private newsService: NewsService) { }

  ngOnInit(): void {
    this.loading = true;
    if(this.variantLocal.isRegion) {
      this.getAllRegionNews()
    } else if(this.variantLocal.isState) {
      this.getAllStateNews();
    } else if(this.variantLocal.isCounty) {
      this.getAllCountiesNews();
    }
  }

  ngOnDestroy() {
    this.destroy$.next(true);
  }

  getAllRegionNews() {
    let regionId: number;
      if(this.variantLocal.id === 'Norte')
        regionId = 1
      else if(this.variantLocal.id === 'Nordeste')
        regionId = 2
      else if(this.variantLocal.id === 'Sudeste')
        regionId = 3
      else if(this.variantLocal.id === 'Sul')
        regionId = 4
      else if(this.variantLocal.id === 'Centro-Oeste')
        regionId = 5
      this.newsService.listAllRegionNews(regionId).pipe(
        takeUntil(this.destroy$)
      ).subscribe(news => {
        this.news = news;
        this.loading = false;
      })
  }

  getAllStateNews() {
    this.newsService.listAllStateNews(this.variantLocal.id).pipe(
      takeUntil(this.destroy$)
    ).subscribe(news => {
      this.news = news;
      this.loading = false;
    })
  }

  getAllCountiesNews() {
    this.newsService.listAllCountyNews(this.variantStateId, this.variantLocal.id).pipe(
      takeUntil(this.destroy$)
    ).subscribe(news => {
      this.news = news;
      this.loading = false;
    })
  }

  closeNewsModal() {
    this.close.emit();
  }

}
