import { Directive, Input, ElementRef } from '@angular/core';

@Directive({
  selector: '[scrollableItem]'
})
export class ScrollableItemDirective {

  @Input('scrollableItem') public id: string
  constructor(private el: ElementRef<HTMLElement>) {}

  public scrollIntoView() {
    console.log("scrollIntoView!!!!");
    console.log("!!!: ", this.id);
    this.el.nativeElement.scrollIntoView({ behavior: 'smooth'});
  }

}