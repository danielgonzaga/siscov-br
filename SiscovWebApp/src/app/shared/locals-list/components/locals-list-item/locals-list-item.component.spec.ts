import { ComponentFixture, TestBed } from '@angular/core/testing';

import { LocalsListItemComponent } from './locals-list-item.component';

describe('LocalsListItemComponent', () => {
  let component: LocalsListItemComponent;
  let fixture: ComponentFixture<LocalsListItemComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ LocalsListItemComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(LocalsListItemComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
