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
      console.log("region varianLocal: ", this.variantLocal);
      // this.newsService.listAllRegionNews(this.variantLocal.id).pipe(
      //   takeUntil(this.destroy$)
      // ).subscribe(news => {
      //   this.news = news;
      //   this.loading = false;
      // })
    } else if(this.variantLocal.isState) {
      this.newsService.listAllStateNews(this.variantLocal.id).pipe(
        takeUntil(this.destroy$)
      ).subscribe(news => {
        console.log("variantLocal from state: ", this.variantLocal);
        this.news = news;
        this.loading = false;
      })
    } else if(this.variantLocal.isCounty) {
      this.newsService.listAllCountyNews(this.variantStateId, this.variantLocal.id).pipe(
        takeUntil(this.destroy$)
      ).subscribe(news => {
        this.news = news;
        this.loading = false;
      })
    }
  }

  ngOnDestroy() {
    console.log("ngOnDestroy!");
    this.destroy$.next(true);
  }

  closeNewsModal() {
    this.close.emit();
  }

}
